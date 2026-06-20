from decimal import Decimal

class Money:
    def __init__(self, amount):
        self.amount = Decimal(str(amount))

    def subtract(self, other):
        return self.amount - other.amount

if __name__ == '__main__':
    money_a = Money(10.50)
    money_b = Money(3.25)
    difference = money_a.subtract(money_b)
    print(difference)