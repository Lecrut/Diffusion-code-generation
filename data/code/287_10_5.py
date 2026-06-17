class WeightSystemConverter:
    def convert_to_kg(self, weight, unit):
        weight = float(weight)
        if unit == 'kg':
            return weight
        elif unit == 'lb':
            return weight * 0.453592
        elif unit == 'g':
            return weight / 1000.0
        else:
            raise ValueError("Invalid unit specified. Supported units are 'kg', 'lb', and 'g'.")
    def convert_to_lb(self, weight, unit):
        weight = float(weight)
        if unit == 'lb':
            return weight
        elif unit == 'kg':
            return weight * 2.20462
        elif unit == 'g':
            return weight / 453.592
        else:
            raise ValueError("Invalid unit specified. Supported units are 'kg', 'lb', and 'g'.")
    def convert_to_g(self, weight, unit):
        weight = float(weight)
        if unit == 'g':
            return weight
        elif unit == 'kg':
            return weight * 1000.0
        elif unit == 'lb':
            return weight * 453.592
        else:
            raise ValueError("Invalid unit specified. Supported units are 'kg', 'lb', and 'g'.")
if __name__ == '__main__':
    converter = WeightSystemConverter()
    print("--- Testing Conversions ---")
    pounds_value = 150.0
    try:
        kg_result = converter.convert_to_kg(pounds_value, 'lb')
        print(f"{pounds_value} lb is equal to {kg_result:.2f} kg")
    except ValueError as e:
        print(f"Error in Test 1: {e}")
    grams_value = 5000.0
    try:
        lb_result = converter.convert_to_lb(grams_value, 'g')
        print(f"{grams_value} g is equal to {lb_result:.2f} lb")
    except ValueError as e:
        print(f"Error in Test 2: {e}")
    kg_value = 2.5
    try:
        g_result = converter.convert_to_g(kg_value, 'kg')
        print(f"{kg_value} kg is equal to {g_result:.2f} g")
    except ValueError as e:
        print(f"Error in Test 3: {e}")
    pounds_direct = 10.0
    try:
        lb_result = converter.convert_to_lb(pounds_direct, 'lb')
        print(f"{pounds_direct} lb is equal to {lb_result:.2f} lb")
    except ValueError as e:
        print(f"Error in Test 4: {e}")
    invalid_value = 100.0
    try:
        converter.convert_to_kg(invalid_value, 'ton')
    except ValueError as e:
        print(f"Error in Test 5 (Expected Failure): {e}")