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
    def to_base(self, value, unit):
        if unit not in self.conversions:
            raise ValueError("Invalid unit provided.")
        return value * self.conversions[unit]
if __name__ == '__main__':
    system = WeightSystem()
    print("--- Conversion Tests ---")
    try:
        kg_value = 1.0
        lbs_result = system.convert(kg_value, 'kg', 'lbs')
        print(f"{kg_value} kg is {lbs_result:.2f} lbs")
        lbs_value = 10.0
        kg_result = system.convert(lbs_value, 'lbs', 'kg')
        print(f"{lbs_value} lbs is {kg_result:.2f} kg")
        grams_value = 500.0
        kg_result_2 = system.convert(grams_value, 'grams', 'kg')
        print(f"{grams_value} grams is {kg_result_2:.2f} kg")
        same_unit = 10
        result_same = system.convert(same_unit, 'kg', 'kg')
        print(f"{same_unit} kg is {result_same} kg")
    except ValueError as e:
        print(f"Error during conversion: {e}")
    print("\n--- Error Handling Tests ---")
    try:
        system.convert(10, 'ton', 'kg')
    except ValueError as e:
        print(f"Caught expected error for invalid 'from' unit: {e}")
    try:
        system.convert(10, 'kg', 'furlongs')
    except ValueError as e:
        print(f"Caught expected error for invalid 'to' unit: {e}")