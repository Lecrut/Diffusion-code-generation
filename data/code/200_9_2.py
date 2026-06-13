def process_complex_objects(data):
    result = []
    for obj in data:
        if hasattr(obj, 'value') and hasattr(obj, 'multiplier'):
            processed_value = obj.value * obj.multiplier
            result.append(processed_value)
    return result
if __name__ == '__main__':
    sample_data = [
        {'value': 10, 'multiplier': 2},
        {'value': 5, 'multiplier': 3},
        {'value': 20, 'multiplier': 1},
        {'value': 8, 'multiplier': 4},
        {'name': 'ignore_me'}
    ]
    final_results = process_complex_objects(sample_data)
    print(final_results)