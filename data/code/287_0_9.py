class WeightSystem:
    def __init__(self):
        self.conversions = {
            'kg': 1.0,
            'lbs': 0.453592,
            'grams': 0.001
        }
    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversions or to_unit not in self.conversions:
            raise ValueError("Invalid unit provided.")
        if from_unit == to_unit:
            return value
        value_in_base = value * self.conversions[from_unit]
        result = value_in_base / self.conversions[to_unit]
        return result
    def to_kg(self, value, unit):
        if unit not in self.conversions:
            raise ValueError("Invalid unit provided.")
        if unit == 'kg':
            return value
        elif unit == 'lbs':
            return value * 0.453592
        elif unit == 'grams':
            return value * 0.001
        else:
            raise ValueError("Unsupported unit for direct conversion.")
if __name__ == '__main__':
    system = WeightSystem()
    print("--- Testing Direct Conversions (to_kg) ---")
    try:
        result1 = system.to_kg(10, 'kg')
        print(f"10 kg to kg: {result1}")
        result2 = system.to_kg(10, 'lbs')
        print(f"10 lbs to kg: {result2:.4f}")
        result3 = system.to_kg(5000, 'grams')
        print(f"5000 grams to kg: {result3:.4f}")
    except ValueError as e:
        print(f"Error during direct conversion: {e}")
    print("\n--- Testing Conversion Method ---")
    try:
        value_lbs = 10
        from_unit = 'lbs'
        to_unit = 'kg'
        result4 = system.convert(value_lbs, from_unit, to_unit)
        print(f"{value_lbs} lbs converted to kg: {result4:.4f}")
        value_grams = 2000
        from_unit = 'grams'
        to_unit = 'lbs'
        result5 = system.convert(value_grams, from_unit, to_unit)
        print(f"{value_grams} grams converted to lbs: {result5:.4f}")
    except ValueError as e:
        print(f"Error during conversion: {e}")
    print("\n--- Testing Error Handling ---")
    try:
        system.convert(10, 'abc', 'kg')
    except ValueError as e:
        print(f"Caught expected error for invalid unit input: {e}")
    try:
        system.convert(10, 'kg', 'tonnes')
    except ValueError as e:
        print(f"Caught expected error for unsupported target unit: {e}")