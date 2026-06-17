class WeightSystem:
    def __init__(self):
        self.conversions = {
            'kg': 1.0,
            'lbs': 0.453592,
            'grams': 0.001
        }
    def to_base(self, weight, unit):
        unit = unit.lower()
        if unit not in self.conversions:
            raise ValueError(f"Invalid unit: {unit}. Supported units are kg, lbs, grams.")
        if unit == 'kg':
            return weight
        elif unit == 'lbs':
            return weight * self.conversions['lbs']
        elif unit == 'grams':
            return weight * self.conversions['grams']
        else:
            raise ValueError(f"Internal error processing unit: {unit}")
    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversions or to_unit not in self.conversions:
            raise ValueError("One or both units are invalid.")
        if from_unit == to_unit:
            return value
        value_in_base = self.to_base(value, from_unit)
        result = value_in_base / self.conversions[to_unit]
        return result
if __name__ == '__main__':
    system = WeightSystem()
    print("--- Testing direct conversion (to base) ---")
    try:
        kg_value = 10.0
        print(f"{kg_value} kg is {system.to_base(kg_value, 'kg'):.2f} kg")
        lbs_value = 5.0
        print(f"{lbs_value} lbs is {system.to_base(lbs_value, 'lbs'):.2f} kg")
        grams_value = 2500.0
        print(f"{grams_value} grams is {system.to_base(grams_value, 'grams'):.2f} kg")
    except ValueError as e:
        print(f"Error during direct conversion: {e}")
    print("\n--- Testing complex conversion ---")
    try:
        lbs_to_kg = system.convert(10, 'lbs', 'kg')
        print(f"10 lbs is {lbs_to_kg:.4f} kg")
        grams_to_lbs = system.convert(500, 'grams', 'lbs')
        print(f"500 grams is {grams_to_lbs:.4f} lbs")
        kg_to_grams = system.convert(2.5, 'kg', 'grams')
        print(f"2.5 kg is {kg_to_grams:.2f} grams")
    except ValueError as e:
        print(f"Error during conversion: {e}")
    print("\n--- Testing error handling ---")
    try:
        system.to_base(10, 'tonnes')
    except ValueError as e:
        print(f"Caught expected error for invalid unit: {e}")
    try:
        system.convert(10, 'kg', 'furlongs')
    except ValueError as e:
        print(f"Caught expected error for invalid conversion: {e}")