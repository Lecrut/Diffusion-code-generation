def sort_by_length_exceeding_ten(items):
    if not isinstance(items, list):
        raise TypeError("Input must be a list.")
    filtered_items = [item for item in items if len(str(item)) > 10]
    try:
        return sorted(filtered_items)
    except Exception as e:
        raise RuntimeError(f"Sorting failed due to error: {e}")
if __name__ == '__main__':
    sample_data = ["hello", "a very long string here", "test", "another short one"]
    try:
        result = sort_by_length_exceeding_ten(sample_data)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")