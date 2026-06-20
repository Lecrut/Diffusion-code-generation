class DecimalMultiplier:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def multiply(self):
        from decimal import Decimal, getcontext
        getcontext().prec = 50
        return Decimal(self.a) * Decimal(self.b)
if __name__ == '__main__':
    multiplier = DecimalMultiplier(0.1, 0.2)
    result = multiplier.multiply()
    print(result)