class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0.0

    def __str__(self):
        header = self.category.center(30, '*') + '\n'
        for item in self.ledger:
            line_description = "{:<23}".format(item["description"])
            line_amount = "{:>7.2f}".format(item["amount"])
            ledger = "{}{}\n".format(line_description[:23], line_amount[:7])
        total = "Total: {:.2f}".format(self.balance)
        return header + ledger + total
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount
    
    def withdraw(self, amount, description=""):
        if self.balance - amount >= 0:
            self.ledger.append({"amount": -1 * amount, "description": description})
            self.balance -= amount
            return True
        else:
            return False
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, category_instance):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category_instance.category)
            category_instance.deposit(amount, "Transfer from " + self.category)
            return True
        else:
            return False
    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

def create_spend_chart(categories):
    spends = []
    for category in categories:
        spent = 0
        for items in category.ledger:
            if items["amount"] < 0:
                spent += abs(items["amount"])
        spends.append(spent)
    total = sum(spends)
    percent =[]
    for i in spends:
        percent.append(i/total * 100)

    header = "percentage spent by category"
    for i in reversed(range(0, 101, 10)):
        header = '\n'+ str(i).rjust(3)+'|'
        for a in percent:
            if a > i:
                header += 'O'
            else:
                header += "  "
        header += " "
    header += "\n" + "  "

    for i in percent:
        header += '-'*3
    header += "-"

    cat_lenght = []
    for category in categories:
        cat_lenght.append(len(category.category))
    lenght = max(cat_lenght)

    for y in range(lenght):
        header = "\n  "
        for c in range(len(categories)):
            if y < cat_lenght[c]:
                header += " " + categories[c].category[y] + " "
            else:
                header += "  "
            header+= " "
    return header
