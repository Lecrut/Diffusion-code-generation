import math
def convert_measurements(data):
    results = {}
    for key, value in data.items():
        if key == 'length':
            metric_value = value * 0.3048
            imperial_value = value
            results[f'{key}_metric'] = metric_value
            results[f'{key}_imperial'] = imperial_value
        elif key == 'weight':
            metric_value = value * 0.45359237
            imperial_value = value
            results[f'{key}_metric'] = metric_value
            results[f'{key}_imperial'] = imperial_value
        elif key == 'volume':
            metric_value = value * 3.785411784
            imperial_value = value
            results[f'{key}_metric'] = metric_value
            results[f'{key}_imperial'] = imperial_value
        else:
            results[f'{key}_metric'] = value
            results[f'{key}_imperial'] = value
    return results
if __name__ == '__main__':
    sample_data = {
        'length': 10.0,
        'weight': 150.0,
        'volume': 5.0
    }
    converted_data = convert_measurements(sample_data)
    print(converted_data)