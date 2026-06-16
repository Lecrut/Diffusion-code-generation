class WeightSystemConverter:
    def convert(self, value, from_unit, to_unit):
        if not isinstance(value, (int, float)):
            raise ValueError("Input value must be a number.")
        if from_unit == to_unit:
            return value
        conversion_factors = {
            'kg': 1000.0,
            'g': 1.0,
            'lb': 2.20462,
            'oz': 35.2739
        }
        if from_unit not in conversion_factors or to_unit not in conversion_factors:
            raise ValueError("Invalid unit specified.")
        if from_unit == 'kg':
            value_in_base = value
        elif from_unit == 'g':
            value_in_base = value / 1000.0
        elif from_unit == 'lb':
            value_in_base = value * 0.453592
        elif from_unit == 'oz':
            value_in_base = value / 35.2739
        else:
            raise ValueError("Unsupported source unit.")
        if to_unit == 'kg':
            result = value_in_base
        elif to_unit == 'g':
            result = value_in_base * 1000.0
        elif to_unit == 'lb':
            result = value_in_base / 0.453592
        elif to_unit == 'oz':
            result = value_in_base * 35.2739
        else:
            raise ValueError("Unsupported target unit.")
        return result
if __name__ == '__main__':
    converter = WeightSystemConverter()
    print("--- Conversion Tests ---")
    kg_value = 10.0
    try:
        lb_result = converter.convert(kg_value, 'kg', 'lb')
        print(f"{kg_value} kg is equal to {lb_result:.4f} lb")
    except ValueError as e:
        print(f"Error: {e}")
    g_value = 5000.0
    try:
        kg_result = converter.convert(g_value, 'g', 'kg')
        print(f"{g_value} g is equal to {kg_result:.4f} kg")
    except ValueError as e:
        print(f"Error: {e}")
    lb_value = 150.0
    try:
        oz_result = converter.convert(lb_value, 'lb', 'oz')
        print(f"{lb_value} lb is equal to {oz_result:.4f} oz")
    except ValueError as e:
        print(f"Error: {e}")
    kg_same = 2.5
    try:
        kg_result_same = converter.convert(kg_same, 'kg', 'kg')
        print(f"{kg_same} kg is equal to {kg_result_same:.4f} kg")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        converter.convert("ten", 'kg', 'lb')
    except ValueError as e:
        print(f"\nCaught expected error for invalid input type: {e}")
    try:
        converter.convert(10, 'ton', 'kg')
    except ValueError as e:
        print(f"Caught expected error for invalid unit: {e}")