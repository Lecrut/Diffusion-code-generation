def get_last_item(data):
    if isinstance(data, list) and len(data) > 0:
        return data[-1]
    elif isinstance(data, tuple) and len(data) > 0:
        return data[-1]
    raise ValueError("Input must be a non-empty sequence.")
if __name__ == '__main__':
    sample_data = [[1, [2, [3]]], "apple", {"key": "value"}]
    result_nested = get_last_item(sample_data[0])
    print(f"Nested last item: {result_nested}")
    try:
        result_string = get_last_item("hello")
        print(f"String last char: '{result_string}'")
    except ValueError:
        pass
    try:
        result_dict = get_last_item(sample_data[2])
    except ValueError as e:
        print(f"Error for dict input (expected): {e}")
    empty_list = []
    try:
        get_last_item(empty_list)
    except ValueError as e:
        print(f"Empty list error (expected): {e}")