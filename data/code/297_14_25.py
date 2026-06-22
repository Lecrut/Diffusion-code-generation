class LengthConverter:
    def __init__(self):
        self.factor = 2.54

    def inches_to_cm(self, inches):
        return inches * self.factor

    def cm_to_inches(self, cm):
        return cm / self.factor

if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.inches_to_cm(1))
    print(converter.inches_to_cm(0.5))
    print(converter.cm_to_inches(2.54))
    print(converter.cm_to_inches(12.7))