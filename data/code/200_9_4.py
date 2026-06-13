def process_complex_objects(data):
    result = []
    for obj in data:
        if hasattr(obj, 'value') and isinstance(obj.value, (int, float)):
            processed_value = obj.value * 2
            result.append(processed_value)
        else:
            result.append(None)
    return result
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'value': 10},
        {'id': 2, 'value': 25.5},
        {'id': 3, 'name': 'A'},
        {'id': 4, 'value': 5}
    ]
    final_results = process_complex_objects(sample_data)
    print(final_results)