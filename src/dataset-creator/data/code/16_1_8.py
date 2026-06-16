def count_top_level_items(items):
    if not isinstance(items, list):
        raise TypeError("Input must be a list.")
    return len([item for item in items])
if __name__ == '__main__':
    sample_data = [1, "apple", {"key": "value"}, True]
    try:
        result = count_top_level_items(sample_data)
        print(f"Number of top-level items: {result}")
    except (TypeError, IndexError) as e:
        print(f"Error occurred: {e}")