class WeightSystemConverter:
    def convert(self, value, from_unit, to_unit):
        if not isinstance(value, (int, float)):
            raise TypeError("Input value must be a number.")
        if not isinstance(from_unit, str) or not isinstance(to_unit, str):
            raise TypeError("Units must be provided as strings.")
        if from_unit == to_unit:
            return value
        if from_unit == "kg":
            if to_unit == "lb":
                return value * 2.2046226218
            elif to_unit == "g":
                return value * 1000.0
            else:
                raise ValueError(f"Unsupported target unit: {to_unit}")
        elif from_unit == "lb":
            if to_unit == "kg":
                return value / 2.2046226218
            elif to_unit == "g":
                return value * 453.59237
            else:
                raise ValueError(f"Unsupported target unit: {to_unit}")
        elif from_unit == "g":
            if to_unit == "kg":
                return value / 1000.0
            elif to_unit == "lb":
                return value / 453.59237
            else:
                raise ValueError(f"Unsupported target unit: {to_unit}")
        else:
            raise ValueError(f"Unsupported source unit: {from_unit}")
if __name__ == '__main__':
    converter = WeightSystemConverter()
    print("--- Conversion Tests ---")
    kg_value = 10
    try:
        result1 = converter.convert(kg_value, "kg", "lb")
        print(f"{kg_value} kg is {result1:.2f} lb")
    except Exception as e:
        print(f"Error in Test 1: {e}")
    lb_value = 50
    try:
        result2 = converter.convert(lb_value, "lb", "kg")
        print(f"{lb_value} lb is {result2:.2f} kg")
    except Exception as e:
        print(f"Error in Test 2: {e}")
    g_value = 2500
    try:
        result3 = converter.convert(g_value, "g", "kg")
        print(f"{g_value} g is {result3:.4f} kg")
    except Exception as e:
        print(f"Error in Test 3: {e}")
    same_unit = 100
    try:
        result4 = converter.convert(same_unit, "kg", "kg")
        print(f"{same_unit} kg is {result4:.2f} kg")
    except Exception as e:
        print(f"Error in Test 4: {e}")
    try:
        converter.convert(10, "kg", "ton")
    except ValueError as e:
        print(f"\nCaught expected error for invalid target unit: {e}")
    except Exception as e:
        print(f"Caught unexpected error in Test 5: {e}")
    try:
        converter.convert(10, "ton", "kg")
    except ValueError as e:
        print(f"Caught expected error for invalid source unit: {e}")
    except Exception as e:
        print(f"Caught unexpected error in Test 6: {e}")
    try:
        converter.convert("ten", "kg", "lb")
    except TypeError as e:
        print(f"Caught expected error for invalid input type: {e}")
    except Exception as e:
        print(f"Caught unexpected error in Test 7: {e}")