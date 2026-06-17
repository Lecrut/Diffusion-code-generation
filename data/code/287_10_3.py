class WeightSystemConverter:
    def convert(self, value, from_unit, to_unit):
        if not isinstance(value, (int, float)):
            raise TypeError("Input value must be a number.")
        if not isinstance(from_unit, str) or not isinstance(to_unit, str):
            raise TypeError("Unit inputs must be strings.")
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
            value_in_grams = value * 1000.0
        elif from_unit == 'g':
            value_in_grams = value
        elif from_unit == 'lb':
            value_in_grams = value * 453.592
        elif from_unit == 'oz':
            value_in_grams = value * 28.3495
        else:
            raise ValueError(f"Unsupported source unit: {from_unit}")
        if to_unit == 'kg':
            result = value_in_grams / 1000.0
        elif to_unit == 'g':
            result = value_in_grams
        elif to_unit == 'lb':
            result = value_in_grams / 453.592
        elif to_unit == 'oz':
            result = value_in_grams / 28.3495
        else:
            raise ValueError(f"Unsupported target unit: {to_unit}")
        return result
if __name__ == '__main__':
    converter = WeightSystemConverter()
    print("--- Test Case 1: Kilograms to Pounds ---")
    try:
        result1 = converter.convert(5, 'kg', 'lb')
        print(f"5 kg is {result1:.2f} lb")
    except Exception as e:
        print(f"Error: {e}")
    print("\n--- Test Case 2: Grams to Kilograms ---")
    try:
        result2 = converter.convert(2500, 'g', 'kg')
        print(f"2500 g is {result2:.3f} kg")
    except Exception as e:
        print(f"Error: {e}")
    print("\n--- Test Case 3: Pounds to Ounces ---")
    try:
        result3 = converter.convert(10, 'lb', 'oz')
        print(f"10 lb is {result3:.2f} oz")
    except Exception as e:
        print(f"Error: {e}")
    print("\n--- Test Case 4: Same Unit Conversion ---")
    try:
        result4 = converter.convert(100, 'g', 'g')
        print(f"100 g is {result4:.2f} g")
    except Exception as e:
        print(f"Error: {e}")
    print("\n--- Test Case 5: Invalid Unit Error ---")
    try:
        converter.convert(10, 'kg', 'ton')
    except ValueError as e:
        print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"Caught unexpected error: {e}")
    print("\n--- Test Case 6: Invalid Input Type Error ---")
    try:
        converter.convert("ten", 'kg', 'lb')
    except TypeError as e:
        print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"Caught unexpected error: {e}")