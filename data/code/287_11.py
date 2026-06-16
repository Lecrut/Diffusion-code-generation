import numpy as np
def convert_weights(raw_weights):
    if not raw_weights:
        return []
    converted_weights = []
    for weight in raw_weights:
        if isinstance(weight, (int, float)):
            if weight[0] == 'kg':
                converted_weights.append(float(weight[1]))
            elif weight[0] == 'g':
                converted_weights.append(float(weight[1]) / 1000)
            elif weight[0] == 'lb':
                converted_weights.append(float(weight[1]) * 0.453592)
        else:
            try:
                if weight[0] == 'kg':
                    converted_weights.append(float(weight[1]))
                elif weight[0] == 'g':
                    converted_weights.append(float(weight[1]) / 1000)
                elif weight[0] == 'lb':
                    converted_weights.append(float(weight[1]) * 0.453592)
            except (TypeError, IndexError):
                pass
    return converted_weights
if __name__ == '__main__':
    sample_data = [
        ('kg', 10.5),
        ('g', 500),
        ('lb', 150.0),
        ('kg', 2.1),
        ('g', 100)
    ]
    def process_sample(data):
        results = []
        for unit, value in data:
            if unit == 'kg':
                result = float(value)
            elif unit == 'g':
                result = float(value) / 1000.0
            elif unit == 'lb':
                result = float(value) * 0.453592
            else:
                result = None
            results.append(result)
        return results
    final_weights = process_sample(sample_data)
    print(final_weights)