def get_unique_sorted_items(input_string):
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")
    items = set(input_string)
    sorted_items = sorted(list(items))
    return sorted_items
if __name__ == '__main__':
    sample_input_1 = "cbaabc"
    sample_input_2 = "programmingisawesome"
    sample_input_3 = "hello world hello"
    sample_input_4 = 12345
    sample_input_5 = ""
    print(f"Input: '{sample_input_1}' -> Output: {get_unique_sorted_items(sample_input_1)}")
    print(f"Input: '{sample_input_2}' -> Output: {get_unique_sorted_items(sample_input_2)}")
    print(f"Input: '{sample_input_3}' -> Output: {get_unique_sorted_items(sample_input_3)}")
    try:
        get_unique_sorted_items(sample_input_4)
    except TypeError as e:
        print(f"Error handling for non-string input (12345): {e}")
    print(f"Input: '{sample_input_5}' -> Output: {get_unique_sorted_items(sample_input_5)}")