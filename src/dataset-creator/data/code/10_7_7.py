def sort_by_length_exceeding_ten(items):
    if not isinstance(items, list):
        raise TypeError("Input must be a list.")
    for item in items:
        if not isinstance(item, str):
            raise ValueError(f"All elements must be strings. Got {type(item).__name__}.")
    sorted_items = [item for item in items if len(item) > 10]
    return sorted(sorted_items, key=len)
if __name__ == '__main__':
    sample_data = ["hello", "worldthisislongerthanfivechars", "abcde", "mediumlengthstring"]
    try:
        result = sort_by_length_exceeding_ten(sample_data)
        print("Sorted items:", result)
    except (TypeError, ValueError) as e:
        print(f"Error occurred: {e}")