import numpy as np
def convert_weights(raw_weights):
    if not raw_weights:
        return []
    converted_weights = []
    for weight in raw_weights:
        if isinstance(weight, (int, float)):
            if weight[0] == 'kg':
                converted_weights.append(float(weight[1]))
            elif weight[0] == 'lb':
                converted_weights.append(float(weight[1]) * 0.453592)
            elif weight[0] == 'g':
                converted_weights.append(float(weight[1]) / 1000)
        else:
            try:
                if isinstance(weight, (int, float)):
                    converted_weights.append(float(weight))
            except ValueError:
                pass
    return converted_weights
if __name__ == '__main__':
    raw_data = [
        ('kg', 10.5),
        ('lb', 150.0),
        ('g', 5000),
        ('kg', 2.3),
        ('lb', 5.5)
    ]
    if not raw_data:
        final_weights = []
    else:
        final_weights = convert_weights(raw_data)
    print(final_weights)