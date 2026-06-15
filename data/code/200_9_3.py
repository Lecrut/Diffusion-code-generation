def process_complex_objects(data):
    result = []
    for obj in data:
        processed_value = obj['value'] * 2 + obj['multiplier']
        result.append(processed_value)
    return result
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'value': 10, 'multiplier': 5},
        {'id': 2, 'value': 20, 'multiplier': 3},
        {'id': 3, 'value': 5, 'multiplier': 10}
    ]
    final_results = process_complex_objects(sample_data)
    print(final_results)