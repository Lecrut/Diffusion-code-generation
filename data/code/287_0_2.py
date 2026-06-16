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
        value_in_kg = value * self.conversions[from_unit]
        result = value_in_kg / self.conversions[to_unit]
        return result
    def to_kg(self, value, unit):
        if unit not in self.conversions:
            raise ValueError("Invalid unit provided.")
        if unit == 'kg':
            return value
        elif unit == 'lbs':
            return value * self.conversions['lbs']
        elif unit == 'grams':
            return value * self.conversions['grams']
        else:
            raise ValueError("Unsupported unit for direct conversion.")
if __name__ == '__main__':
    system = WeightSystem()
    print("--- Testing Conversion ---")
    try:
        result1 = system.convert(10, 'kg', 'lbs')
        print(f"10 kg is {result1:.2f} lbs")
        result2 = system.convert(500, 'grams', 'kg')
        print(f"500 grams is {result2:.2f} kg")
        result3 = system.convert(2, 'lbs', 'grams')
        print(f"2 lbs is {result3:.2f} grams")
    except ValueError as e:
        print(f"Error during conversion: {e}")
    print("\n--- Testing Direct Conversion (to_kg) ---")
    try:
        result4 = system.to_kg(150, 'lbs')
        print(f"150 lbs is {result4:.2f} kg")
        result5 = system.to_kg(3000, 'grams')
        print(f"3000 grams is {result5:.2f} kg")
    except ValueError as e:
        print(f"Error during direct conversion: {e}")
    print("\n--- Testing Error Handling ---")
    try:
        system.convert(10, 'tonnes', 'kg')
    except ValueError as e:
        print(f"Caught expected error for invalid unit in convert: {e}")
    try:
        system.to_kg(10, 'furlongs')
    except ValueError as e:
        print(f"Caught expected error for invalid unit in to_kg: {e}")