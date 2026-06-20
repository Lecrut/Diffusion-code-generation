class DecimalMultiplier:
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def multiply(self, number):
        return number * self.multiplier

if __name__ == '__main__':
    dm = DecimalMultiplier(10)
    result = dm.multiply(0.5)
    print(result)