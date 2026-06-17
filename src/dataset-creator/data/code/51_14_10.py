def get_first_element(data):
    if data is None:
        raise ValueError("Input cannot be null.")
    if not isinstance(data, list):
        raise TypeError(f"Expected a list, got {type(data).__name__}.")
    if len(data) == 0:
        return "No elements available."
    return data[0]
if __name__ == '__main__':
    try:
        sample_data = [10, 20, 30]
        result = get_first_element(sample_data)
        print(f"First element of {sample_data} is: {result}")
        null_input = None
        empty_list = []
        test_cases = [null_input, "string", 42]
        for item in test_cases:
            try:
                output = get_first_element(item)
                print(f"Input {item} -> Output: {output}")
            except (ValueError, TypeError) as e:
                print(f"Input {item} raised exception: {e}")
    except Exception as general_error:
        print(f"Unexpected error occurred: {general_error}")