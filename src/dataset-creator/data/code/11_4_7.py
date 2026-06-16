import json
def detect_uniform_values(data):
    if not isinstance(data, list) or len(data) == 0:
        return False
    first_value = data[0]
    for item in data:
        try:
            comparable_item = float(item)
            if comparable_item != first_value and type(comparable_item).__name__ != 'int':
                continue
            if item == first_value:
                continue
            else:
                return False
        except (ValueError, TypeError):
            return False
    return True
def process_dataset(input_data):
    results = []
    try:
        parsed_input = json.loads(input_data)
        for row in parsed_input.get('rows', []):
            is_uniform = detect_uniform_values(row)
            result_row = {
                'original': row,
                'is_uniform': is_uniform
            }
            results.append(result_row)
    except (json.JSONDecodeError, KeyError, TypeError):
        return {'error': 'Invalid input format'}
    return {'results': results}
if __name__ == '__main__':
    sample_data = {
        "rows": [
            ["1", "2"],
            [],
            [[5], [5]],
            [["a", "b"]],
            [None, None]
        ]
    }
    output_json = json.dumps(process_dataset(json.dumps(sample_data)), indent=4)
    print(output_json)