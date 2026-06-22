class InchToCmConverter:

    def __init__(self):
        self.conversion_factor = 2.54

    def convert(self, inches):
        return inches * self.conversion_factor
if __name__ == '__main__':
    converter = InchToCmConverter()
    result1 = converter.convert(1)
    print(result1)
    result2 = converter.convert(10)
    print(result2)