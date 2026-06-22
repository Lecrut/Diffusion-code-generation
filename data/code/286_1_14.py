class LengthConverter:
    def __init__(self, feet):
        self.feet = feet

    def convert_to_meters(self):
        if not isinstance(self.feet, (int, float)):
            raise ValueError("Input must be a number")
        return self.feet * 0.3048

if __name__ == '__main__':
    converter = LengthConverter(10)
    print(converter.convert_to_meters())