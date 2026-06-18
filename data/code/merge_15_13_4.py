def get_unique_sorted_items(input_string):
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")
    items = set(input_string)
    sorted_items = sorted(list(items))
    return sorted_items
if __name__ == '__main__':
    sample_input = "cbaabcde"
    try:
        result = get_unique_sorted_items(sample_input)
        print(result)
    except TypeError as e:
        print(f"Error: {e}")
    sample_input_2 = "programmingisawesome"
    try:
        result_2 = get_unique_sorted_items(sample_input_2)
        print(result_2)
    except TypeError as e:
        print(f"Error: {e}")
    sample_input_3 = 12345
    try:
        result_3 = get_unique_sorted_items(sample_input_3)
        print(result_3)
    except TypeError as e:
        print(f"Error: {e}")