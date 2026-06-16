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
        kg_value = 10.0
        lbs_value = 22.0462                       
        grams_value = 9260.82                       
        print(f"{kg_value} kg to lbs: {system.convert(kg_value, 'kg', 'lbs'):.2f} lbs")
        print(f"{lbs_value} lbs to kg: {system.convert(lbs_value, 'lbs', 'kg'):.2f} kg")
        print(f"{grams_value} grams to kg: {system.convert(grams_value, 'grams', 'kg'):.2f} kg")
        print(f"5 kg to grams: {system.to_base(5, 'kg'):.2f} grams")
    except ValueError as e:
        print(f"Error during conversion: {e}")
    print("\n--- Error Handling Tests ---")
    try:
        system.convert(10, 'kg', 'tonnes')
    except ValueError as e:
        print(f"Caught expected error for invalid target unit: {e}")
    try:
        system.convert(10, 'furlongs', 'kg')
    except ValueError as e:
        print(f"Caught expected error for invalid source unit: {e}")