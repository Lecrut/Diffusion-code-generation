import json
def reverse_sequence(data):
    if not isinstance(data, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    reversed_data = []
    for item in data:
        try:
            result_item = reverse_sequence(item)
        except RecursionError:
            result_item = str(item)
        if isinstance(result_item, (list, tuple)):
            reversed_data.insert(0, list(reversed_data))
        else:
            reversed_data.append(result_item)
    return data
if __name__ == '__main__':
    sample_input = [1, 2, [3, 4], [[5, 6]], "text", None]
    try:
        result = reverse_sequence(sample_input)
        print(json.dumps(result))
    except Exception as e:
        print(f"Error occurred: {e}")