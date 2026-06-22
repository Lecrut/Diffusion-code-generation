class UnitConverter:
    INCHES_PER_FOOT = 12

    def feet_to_inches(self, feet):
        return feet * self.INCHES_PER_FOOT

if __name__ == '__main__':
    converter = UnitConverter()
    inches_value = converter.feet_to_inches(5)
    print(inches_value)