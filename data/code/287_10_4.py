class WeightSystemConverter:
    def __init__(self):
        self.conversion_factors = {
            'kg_to_g': 1000,
            'lb_to_g': 453.592,
            'g_to_kg': 0.001,
            'g_to_lb': 0.00220462
        }
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        if from_unit == to_unit:
            return value
        from_unit = from_unit.lower().strip()
        to_unit = to_unit.lower().strip()
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors:
            raise ValueError("Invalid unit specified. Supported units are: kg, lb, g.")
        if from_unit == 'kg' and to_unit == 'g':
            return value * self.conversion_factors['kg_to_g']
        elif from_unit == 'lb' and to_unit == 'g':
            return value * self.conversion_factors['lb_to_g']
        elif from_unit == 'g' and to_unit == 'kg':
            return value * self.conversion_factors['g_to_kg']
        elif from_unit == 'g' and to_unit == 'lb':
            return value / self.conversion_factors['g_to_lb']
        elif from_unit == 'kg' and to_unit == 'lb':
            return value / 0.453592
        elif from_unit == 'lb' and to_unit == 'kg':
            return value / self.conversion_factors['lb_to_g'] / 1000                                                                         
            return value * (1 / self.conversion_factors['lb_to_g'])
        else:
            raise NotImplementedError(f"Conversion from {from_unit} to {to_unit} is not implemented.")
if __name__ == '__main__':
    converter = WeightSystemConverter()
    print("--- Test Case 1: Kilograms to Grams ---")
    try:
        result1 = converter.convert(5.0, 'kg', 'g')
        print(f"5.0 kg is {result1:.2f} g")
    except Exception as e:
        print(f"Error: {e}")
    print("\n--- Test Case 2: Pounds to Kilograms ---")
    try:
        result2 = converter.convert(150.0, 'lb', 'kg')
        print(f"150.0 lb is {result2:.3f} kg")
    except Exception as e:
        print(f"Error: {e}")
    print("\n--- Test Case 3: Grams to Pounds ---")
    try:
        result3 = converter.convert(2500.0, 'g', 'lb')
        print(f"2500.0 g is {result3:.3f} lb")
    except Exception as e:
        print(f"Error: {e}")
    print("\n--- Test Case 4: Same Unit Conversion ---")
    try:
        result4 = converter.convert(10.0, 'kg', 'kg')
        print(f"10.0 kg is {result4:.2f} kg")
    except Exception as e:
        print(f"Error: {e}")
    print("\n--- Test Case 5: Error Handling (Invalid Unit) ---")
    try:
        converter.convert(10, 'ton', 'kg')
    except ValueError as e:
        print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"Caught unexpected error: {e}")
    print("\n--- Test Case 6: Error Handling (Unsupported Conversion) ---")
    try:
        converter.convert(10, 'lb', 'ton')
    except NotImplementedError as e:
        print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"Caught unexpected error: {e}")