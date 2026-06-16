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
            except:
                pass
    return converted_weights
if __name__ == '__main__':
    sample_data = [
        ('kg', 10.5),
        ('lb', 150.0),
        ('g', 2500),
        ('kg', 5.2),
        ('lb', 300.5)
    ]
    results = convert_weights(sample_data)
    print(results)