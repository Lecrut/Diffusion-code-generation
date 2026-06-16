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
        kg_value = 10.0
        lbs_value = system.convert(kg_value, 'kg', 'lbs')
        print(f"{kg_value} kg is {lbs_value:.2f} lbs")
        grams_value = 500.0
        kg_from_grams = system.convert(grams_value, 'grams', 'kg')
        print(f"{grams_value} grams is {kg_from_grams:.4f} kg")
        same_unit = system.convert(100, 'kg', 'kg')
        print(f"100 kg to kg is {same_unit}")
    except ValueError as e:
        print(f"Error during conversion: {e}")
    print("\n--- Testing Direct Conversion (to_kg) ---")
    try:
        weight_lbs = 220.462                 
        kg_result = system.to_kg(weight_lbs, 'lbs')
        print(f"{weight_lbs} lbs is {kg_result:.3f} kg")
        weight_grams = 5000.0
        kg_result_2 = system.to_kg(weight_grams, 'grams')
        print(f"{weight_grams} grams is {kg_result_2:.4f} kg")
    except ValueError as e:
        print(f"Error during direct conversion: {e}")
    print("\n--- Testing Error Handling ---")
    try:
        system.convert(10, 'abc', 'kg')
    except ValueError as e:
        print(f"Caught expected error for invalid unit input: {e}")
    try:
        system.convert(10, 'kg', 'tonnes')
    except ValueError as e:
        print(f"Caught expected error for invalid target unit: {e}")