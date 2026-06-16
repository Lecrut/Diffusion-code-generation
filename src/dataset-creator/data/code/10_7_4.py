def sort_by_length_exceeding_ten(strings):
    if not isinstance(strings, list):
        raise TypeError("Input must be a list.")
    for item in strings:
        if not isinstance(item, str):
            raise ValueError(f"All elements in the input list must be strings. Found {type(item).__name__}.")
    filtered_strings = [s for s in strings if len(s) > 10]
    try:
        sorted_strings = sorted(filtered_strings, key=len)
    except TypeError as e:
        raise RuntimeError(f"Sorting failed due to mixed types or unsortable elements.") from e
    return sorted_strings
if __name__ == '__main__':
    sample_data = ["hello", "worldthisislongstring", "test", "abcdefghij"]
    try:
        result = sort_by_length_exceeding_ten(sample_data)
        print("Sorted strings:", result)
    except (TypeError, ValueError, RuntimeError) as e:
        print(f"An error occurred: {e}")