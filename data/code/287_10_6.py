class WeightSystemConverter:
    def __init__(self):
        self.conversion_factors = {
            'kg_to_g': 1000,
            'lb_to_g': 453.592,
            'g_to_kg': 0.001,
            'g_to_lb': 0.00220462,
            'kg_to_lb': 2.20462,
            'lb_to_kg': 0.453592
        }
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        if from_unit == to_unit:
            return value
        from_unit = from_unit.lower().strip()
        to_unit = to_unit.lower().strip()
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors:
            raise ValueError("Invalid unit specified. Supported units are: kg, lb, g.")
        if from_unit == 'kg' and to_unit == 'lb':
            return value * self.conversion_factors['kg_to_lb']
        elif from_unit == 'lb' and to_unit == 'kg':
            return value * self.conversion_factors['lb_to_kg']
        elif from_unit == 'g' and to_unit == 'kg':
            return value * self.conversion_factors['g_to_kg']
        elif from_unit == 'kg' and to_unit == 'g':
            return value * self.conversion_factors['kg_to_g']
        elif from_unit == 'lb' and to_unit == 'g':
            return value * self.conversion_factors['lb_to_g']
        elif from_unit == 'g' and to_unit == 'lb':
            return value * self.conversion_factors['g_to_lb']
        else:
            raise ValueError("Conversion path not supported for these units.")
if __name__ == '__main__':
    converter = WeightSystemConverter()
    print("--- Test Case 1: Kilograms to Pounds ---")
    try:
        kg_value = 10.0
        lb_result = converter.convert(kg_value, 'kg', 'lb')
        print(f"{kg_value} kg is equal to {lb_result:.2f} lb")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Test Case 2: Pounds to Grams ---")
    try:
        lb_value = 5.0
        g_result = converter.convert(lb_value, 'lb', 'g')
        print(f"{lb_value} lb is equal to {g_result:.2f} g")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Test Case 3: Grams to Kilograms ---")
    try:
        g_value = 5000.0
        kg_result = converter.convert(g_value, 'g', 'kg')
        print(f"{g_value} g is equal to {kg_result:.4f} kg")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Test Case 4: Same Unit Conversion ---")
    try:
        val = 100.0
        same_result = converter.convert(val, 'kg', 'kg')
        print(f"{val} kg is equal to {same_result:.2f} kg")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Test Case 5: Invalid Input Handling ---")
    try:
        converter.convert(10, 'ton', 'kg')
    except ValueError as e:
        print(f"Successfully caught error for invalid input: {e}")
    print("\n--- Test Case 6: Invalid Unit Combination ---")
    try:
        converter.convert(10, 'lb', 'ton')
    except ValueError as e:
        print(f"Successfully caught error for unsupported path: {e}")