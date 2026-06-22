class LengthConverter:
    conversion_factor = 0.3048

    def __init__(self, feet):
        self.feet = feet

    def convert_to_meters(self):
        try:
            return self.feet * self.conversion_factor
        except (ValueError, TypeError):
            return None

if __name__ == '__main__':
    converter = LengthConverter(10)
    result = converter.convert_to_meters()
    print(result)