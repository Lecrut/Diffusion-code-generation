class UnitConverter:
    def __init__(self):
        self.inches_per_foot = 12

    def convert_feet_to_inches(self, feet_value):
        return feet_value * self.inches_per_foot

    def get_conversion_factor(self):
        return self.inches_per_foot

if __name__ == '__main__':
    converter = UnitConverter()
    val1 = converter.convert_feet_to_inches(10)
    val2 = converter.convert_feet_to_inches(3.5)
    factor = converter.get_conversion_factor()
    print(val1)
    print(val2)
    print(factor)