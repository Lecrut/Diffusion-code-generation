def sort_by_length_exceeding_ten(items):
    if not isinstance(items, list):
        raise TypeError("Input must be a list.")
    for item in items:
        if not isinstance(item, str):
            raise ValueError(f"All elements must be strings. Got {type(item).__name__}.")
    filtered_items = [item for item in items if len(item) > 10]
    return sorted(filtered_items, key=len)
if __name__ == '__main__':
    sample_data = ["hello", "worldthisislongerthanbefore", "test", "abcdefghij"]
    try:
        result = sort_by_length_exceeding_ten(sample_data)
        print(result)
    except Exception as e:
        raise RuntimeError(f"An error occurred during processing: {e}") from e