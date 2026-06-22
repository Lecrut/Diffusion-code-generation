class LengthConverter:
    INCHES_PER_FOOT = 12

    def feet_to_inches(self, feet):
        return feet * self.INCHES_PER_FOOT

    def validate_input(self, value):
        return isinstance(value, (int, float)) and value >= 0

if __name__ == '__main__':
    converter = LengthConverter()
    sample_feet = 3.5
    print(converter.validate_input(sample_feet))
    print(converter.feet_to_inches(sample_feet))
    sample_feet_two = 10
    print(converter.feet_to_inches(sample_feet_two))