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
if __name__ == '__main__':
    system = WeightSystem()
    print("--- Conversion Tests ---")
    try:
        kg_value = 10.0
        lbs_result = system.convert(kg_value, 'kg', 'lbs')
        print(f"{kg_value} kg is {lbs_result:.2f} lbs")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        lbs_value = 150.0
        grams_result = system.convert(lbs_value, 'lbs', 'grams')
        print(f"{lbs_value} lbs is {grams_result:.2f} grams")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        grams_value = 5000.0
        kg_result = system.convert(grams_value, 'grams', 'kg')
        print(f"{grams_value} grams is {kg_result:.2f} kg")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        value = 10.0
        same_unit_result = system.convert(value, 'kg', 'kg')
        print(f"{value} kg is {same_unit_result:.2f} kg")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Error Handling Tests ---")
    try:
        system.convert(10, 'ton', 'kg')
    except ValueError as e:
        print(f"Caught expected error for invalid 'from' unit: {e}")
    try:
        system.convert(10, 'kg', 'furlongs')
    except ValueError as e:
        print(f"Caught expected error for invalid 'to' unit: {e}")
    try:
        system.convert(10, 'ton', 'furlongs')
    except ValueError as e:
        print(f"Caught expected error for both invalid units: {e}")