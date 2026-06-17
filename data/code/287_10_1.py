class WeightSystemConverter:
    def convert(self, value, from_unit, to_unit):
        if not isinstance(value, (int, float)):
            raise TypeError("Input value must be a number.")
        conversion_factors = {
            'kg': 1.0,
            'g': 1000.0,
            'lb': 2.20462,
            'oz': 35.2739
        }
        if from_unit not in conversion_factors or to_unit not in conversion_factors:
            raise ValueError("Invalid unit provided.")
        if from_unit == to_unit:
            return value
        value_in_base = value
        if from_unit != 'kg':
            value_in_base = value * conversion_factors[from_unit]
        result = value_in_base / conversion_factors[to_unit]
        return result
if __name__ == '__main__':
    converter = WeightSystemConverter()
    print("--- Conversion Tests ---")
    kg_value = 10.0
    try:
        lb_result = converter.convert(kg_value, 'kg', 'lb')
        print(f"{kg_value} kg is {lb_result:.2f} lb")
    except (TypeError, ValueError) as e:
        print(f"Error in Test 1: {e}")
    g_value = 5000.0
    try:
        kg_result = converter.convert(g_value, 'g', 'kg')
        print(f"{g_value} g is {kg_result:.3f} kg")
    except (TypeError, ValueError) as e:
        print(f"Error in Test 2: {e}")
    lb_value = 150.0
    try:
        g_result = converter.convert(lb_value, 'lb', 'g')
        print(f"{lb_value} lb is {g_result:.2f} g")
    except (TypeError, ValueError) as e:
        print(f"Error in Test 3: {e}")
    same_unit_value = 100
    try:
        same_unit_result = converter.convert(same_unit_value, 'kg', 'kg')
        print(f"{same_unit_value} kg is {same_unit_result:.2f} kg")
    except (TypeError, ValueError) as e:
        print(f"Error in Test 4: {e}")
    print("\n--- Error Handling Tests ---")
    try:
        converter.convert("invalid", 'kg', 'lb')
    except (TypeError, ValueError) as e:
        print(f"Caught expected error for invalid type: {e}")
    try:
        converter.convert(10, 'ton', 'lb')
    except (TypeError, ValueError) as e:
        print(f"Caught expected error for invalid unit: {e}")
    try:
        converter.convert(10, 'kg', 'ton')                                                                                        
    except (TypeError, ValueError) as e:
        print(f"Caught expected error for missing unit context: {e}")