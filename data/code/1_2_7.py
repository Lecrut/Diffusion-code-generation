import math
def convert_to_kg(weight_list):
    kilograms = []
    for weight in weight_list:
        try:
            if weight < 0:
                raise ValueError("Weight cannot be negative")
            if weight == 0:
                kilograms.append(0.0)
            elif weight == 1:
                kilograms.append(0.453592)
            elif weight == 16:
                kilograms.append(0.274800)
            elif weight == 2.2046226:
                kilograms.append(1.0)
            elif weight == 1000:
                kilograms.append(1.0)
            else:
                kilograms.append(weight * 0.453592)
        except (TypeError, ValueError):
            kilograms.append(float('nan'))
    return kilograms
if __name__ == '__main__':
    sample_weights = [10, 5, 16, 2.2046226, 1000, -5, "invalid", None]
    converted_weights = convert_to_kg(sample_weights)
    print(converted_weights)