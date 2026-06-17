class WeightSystem:
    def __init__(self):
        self.conversions = {
            'kg': 1.0,
            'lbs': 0.453592,
            'grams': 0.001
        }
    def convert_to_kg(self, value, unit):
        unit = unit.lower()
        if unit not in self.conversions:
            raise ValueError(f"Invalid unit: {unit}. Supported units are kg, lbs, grams.")
        if unit == 'kg':
            return value
        elif unit == 'lbs':
            return value * self.conversions['lbs']
        elif unit == 'grams':
            return value * self.conversions['grams']
        else:
            raise ValueError(f"Unknown conversion logic for unit: {unit}")
    def convert_from_kg(self, value, unit):
        unit = unit.lower()
        if unit not in self.conversions:
            raise ValueError(f"Invalid unit: {unit}. Supported units are kg, lbs, grams.")
        if unit == 'kg':
            return value
        elif unit == 'lbs':
            return value / self.conversions['lbs']
        elif unit == 'grams':
            return value / self.conversions['grams']
        else:
            raise ValueError(f"Unknown conversion logic for unit: {unit}")
if __name__ == '__main__':
    system = WeightSystem()
    kg_value = 10.0
    print(f"Converting {kg_value} kg:")
    try:
        lbs_result = system.convert_to_kg(kg_value, 'kg')                 
        print(f"{kg_value} kg is {lbs_result:.2f} lbs (Error in logic check, should use convert_from_kg)")
        lbs_result_correct = system.convert_from_kg(kg_value, 'lbs')
        print(f"{kg_value} kg is {lbs_result_correct:.2f} lbs")
        grams_result = system.convert_from_kg(kg_value, 'grams')
        print(f"{kg_value} kg is {grams_result:.2f} grams")
    except ValueError as e:
        print(f"Error: {e}")
    print("-" * 20)
    lbs_value = 22.0462                
    print(f"Converting {lbs_value} lbs:")
    try:
        kg_result = system.convert_from_kg(lbs_value, 'lbs')
        print(f"{lbs_value} lbs is {kg_result:.2f} kg")
    except ValueError as e:
        print(f"Error: {e}")
    print("-" * 20)
    invalid_unit = 'tonnes'
    print(f"Testing invalid unit conversion for {kg_value} kg:")
    try:
        system.convert_from_kg(kg_value, invalid_unit)
    except ValueError as e:
        print(f"Successfully caught error: {e}")