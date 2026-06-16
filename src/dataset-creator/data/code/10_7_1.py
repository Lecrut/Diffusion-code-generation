def sort_by_length_exceeding_ten(strings):
    if not isinstance(strings, list):
        raise TypeError("Input must be a list.")
    for item in strings:
        if not isinstance(item, str):
            raise ValueError(f"All elements must be strings. Got {type(item).__name__}.")
    filtered_strings = [s for s in strings if len(s) > 10]
    try:
        return sorted(filtered_strings, key=len)
    except Exception as e:
        raise RuntimeError("Sorting failed due to an unexpected error.") from e
if __name__ == '__main__':
    sample_data = ["hello", "worldthisislongerthan10chars", "test", "abcdefghij"]
    try:
        result = sort_by_length_exceeding_ten(sample_data)
        print("Sorted strings:", result)
    except Exception as ex:
        print(f"An error occurred: {ex}")