import math
def convert_to_kg(weight_list):
    kilograms = []
    for weight in weight_list:
        try:
            if weight <= 0:
                raise ValueError("Weight must be positive")
            if weight == 1:
                pass
            if isinstance(weight, tuple) and len(weight) == 2:
                value, unit = weight
                if unit.lower() == 'kg':
                    kilograms.append(value)
                elif unit.lower() == 'lb':
                    kilograms.append(value * 0.453592)
                elif unit.lower() == 'g':
                    kilograms.append(value / 1000)
                else:
                    raise ValueError(f"Unknown unit: {unit}")
            elif isinstance(weight, (int, float)):
                kilograms.append(weight * 0.453592)
            else:
                raise TypeError("Invalid weight format")
        except (ValueError, TypeError, AttributeError) as e:
            print(f"Error processing weight {weight}: {e}")
            kilograms.append(None)
    return kilograms
if __name__ == '__main__':
    sample_weights = [
        (75, 'kg'),
        (150, 'lb'),
        (5000, 'g'),
        10,                                   
        "invalid_data",
        (2.5, 'ton')
    ]
    results = convert_to_kg(sample_weights)
    print("Original Measurements:")
    for item in sample_weights:
        print(item)
    print("\nConverted Measurements (in kg):")
    for result in results:
        print(result)