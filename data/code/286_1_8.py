class LengthConverter:
    def __init__(self, feet):
        if not isinstance(feet, (int, float)):
            raise ValueError("Feet value must be an integer or float")
        self.feet = feet

    def to_meters(self):
        meters = self.feet * 0.3048
        return round(meters, 2)

if __name__ == '__main__':
    converter = LengthConverter(10)
    print(converter.to_meters())