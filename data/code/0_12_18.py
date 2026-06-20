class LengthConverter:
    CENTIMETERS_PER_INCH = 2.54

    def convert(self, cm):
        return cm / self.CENTIMETERS_PER_INCH

    def to_inches(self, value):
        return self.convert(value)

if __name__ == '__main__':
    converter = LengthConverter()
    result_50 = converter.to_inches(50)
    print(result_50)
    result_100 = converter.to_inches(100)
    print(result_100)