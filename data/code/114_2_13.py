class DecimalMultiplier:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def multiply(self):
        return self.value1 * self.value2

if __name__ == '__main__':
    multiplier_instance = DecimalMultiplier(0.1, 0.2)
    result = multiplier_instance.multiply()
    print(result)