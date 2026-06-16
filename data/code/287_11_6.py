import numpy as np
def convert_weights(raw_weights):
    if not raw_weights:
        return []
    results = []
    for weight, unit in raw_weights:
        if unit == 'kg':
            converted_weight = weight
        elif unit == 'g':
            converted_weight = weight / 1000.0
        elif unit == 'lb':
            converted_weight = weight * 0.453592
        else:
            raise ValueError(f"Unknown unit: {unit}")
        results.append(converted_weight)
    return results
if __name__ == '__main__':
    raw_data = [
        (100, 'kg'),
        (5000, 'g'),
        (150, 'lb'),
        (2000, 'kg'),
        (1000, 'g'),
        (50, 'lb')
    ]
    standardized_weights = convert_weights(raw_data)
    print(standardized_weights)