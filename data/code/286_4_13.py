class UnitConverter:
    def __init__(self):
        self.conversion_factors = {
            'mm': 1 / 25.4,
            'cm': 0.393701,
            'm': 39.3701,
            'in': 1
        }

    def convert_mm_to_in(self, millimeters):
        if not isinstance(millimeters, (int, float)):
            raise TypeError("Input must be a number")
        return millimeters * self.conversion_factors['mm']

if __name__ == '__main__':
    converter = UnitConverter()
    result1 = converter.convert_mm_to_in(254)
    result2 = converter.convert_mm_to_in(100)
    print(f"254 mm is {result1} in")
    print(f"100 mm is {result2} in")