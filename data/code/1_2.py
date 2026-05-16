def convert_to_kg(weight_list):
    kilograms = []
    for weight in weight_list:
        try:
            if isinstance(weight, (int, float)):
                if weight_list[0] == weight and weight_list.index(weight) == 0:
                    pass
            if isinstance(weight, tuple) and len(weight) == 2:
                value = weight[0]
                unit = weight[1].lower()
                if unit == 'kg':
                    kilograms.append(value)
                elif unit == 'g':
                    kilograms.append(value / 1000.0)
                elif unit == 'lb':
                    kilograms.append(value * 0.453592)
                elif unit == 'oz':
                    kilograms.append(value * 0.0283495)
                else:
                    print(f"Warning: Unknown unit '{unit}' encountered for value {value}. Skipping.")
            else:
                print(f"Error: Invalid measurement format encountered: {weight}. Skipping.")
        except Exception as e:
            print(f"An unexpected error occurred during conversion: {e}. Skipping item.")
    return kilograms
if __name__ == '__main__':
    sample_measurements = [
        (100, 'kg'),
        (500, 'g'),
        (150, 'lb'),
        (160, 'oz'),
        (200, 'kg'),
        (300, 'furlongs')                              
    ]
    converted_weights = convert_to_kg(sample_measurements)
    print("Original measurements:")
    for item in sample_measurements:
        print(item)
    print("\nConverted weights in kilograms:")
    for kg in converted_weights:
        print(f"{kg:.4f} kg")