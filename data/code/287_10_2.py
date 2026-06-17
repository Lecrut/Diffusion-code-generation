class WeightSystemConverter:
    def convert_to_kg(self, weight, unit):
        if unit.lower() == 'kg':
            return weight
        elif unit.lower() == 'lb':
            return weight * 0.453592
        elif unit.lower() == 'g':
            return weight / 1000.0
        else:
            raise ValueError("Invalid unit specified. Supported units are kg, lb, g.")
    def convert_to_lb(self, weight, unit):
        if unit.lower() == 'lb':
            return weight
        elif unit.lower() == 'kg':
            return weight * 2.20462
        elif unit.lower() == 'g':
            return weight / 453.592
        else:
            raise ValueError("Invalid unit specified. Supported units are kg, lb, g.")
    def convert_to_g(self, weight, unit):
        if unit.lower() == 'g':
            return weight
        elif unit.lower() == 'lb':
            return weight * 453.592
        elif unit.lower() == 'kg':
            return weight * 1000.0
        else:
            raise ValueError("Invalid unit specified. Supported units are kg, lb, g.")
if __name__ == '__main__':
    converter = WeightSystemConverter()
    sample_weight = 150
    print("--- Conversion Tests ---")
    try:
        kg_result = converter.convert_to_kg(sample_weight, 'lb')
        print(f"{sample_weight} lb is {kg_result:.2f} kg")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        lb_result = converter.convert_to_lb(sample_weight, 'kg')
        print(f"{sample_weight} kg is {lb_result:.2f} lb")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        g_result = converter.convert_to_g(sample_weight, 'lb')
        print(f"{sample_weight} lb is {g_result:.2f} g")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Error Handling Tests ---")
    try:
        converter.convert_to_kg(10, 'ton')
    except ValueError as e:
        print(f"Caught expected error for invalid unit: {e}")
    try:
        converter.convert_to_lb(50, 'ton')
    except ValueError as e:
        print(f"Caught expected error for invalid unit: {e}")