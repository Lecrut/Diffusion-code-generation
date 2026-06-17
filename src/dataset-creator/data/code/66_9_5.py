import sys
class WeightCalculator:
    def validate_inputs(self, weight1, unit1, weight2, unit2):
        if not isinstance(weight1, (int, float)) or not isinstance(unit1, str) or\
           not isinstance(weight2, (int, float)) or not isinstance(unit2, str):
            raise ValueError("Invalid input types: weights must be numeric and units must be strings.")
        valid_units = ['kg', 'g', 'lb']
        if unit1.lower() not in [u.lower() for u in valid_units] or\
           unit2.lower() not in [u.lower() for u in valid_units]:
            raise ValueError(f"Invalid units: must be one of {valid_units}.")
    def convert_to_base(self, weight, unit):
        base_unit = 'kg'
        if unit == 'g':
            return weight / 1000.0
        elif unit == 'lb':
            return weight * 0.45359237
        else:
            return float(weight)
    def calculate_absolute_difference(self, w1_str, u1_str, w2_str, u2_str):
        self.validate_inputs(w1_str, u1_str, w2_str, u2_str)
        base_w1 = self.convert_to_base(float(w1_str), u1_str.lower())
        base_w2 = self.convert_to_base(float(w2_str), u2_str.lower())
        abs_diff = abs(base_w1 - base_w2)
        return {
            'absolute_difference_kg': round(abs_diff, 4),
            'unit_1_original_value': float(w1_str),
            'unit_2_original_value': float(w2_str)
        }
def main():
    calc = WeightCalculator()
    sample_data = [
        ("75", "kg"),
        ("80.5", "g")
    ]
    try:
        result = calc.calculate_absolute_difference(*sample_data[0], *sample_data[1])
        print("=== Absolute Difference Calculation ===")
        print(f"Input 1: {result['unit_1_original_value']} {sample_data[0][1]}")
        print(f"Input 2: {result['unit_2_original_value']} {sample_data[1][1]}")
        print(f"Absolute Difference (kg): {result['absolute_difference_kg']} kg")
    except ValueError as e:
        print(f"Validation Error: {e}")
if __name__ == '__main__':
    main()