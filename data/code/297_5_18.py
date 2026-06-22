class InchToCmConverter:

    def __init__(self):
        self.conversion_factor = 2.54

    def convert(self, inches):
        return inches * self.conversion_factor
if __name__ == '__main__':
    converter = InchToCmConverter()
    print(converter.convert(1))
    print(converter.convert(10))