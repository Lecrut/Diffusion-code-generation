def count_top_level_items(items):
    if not isinstance(items, list):
        raise TypeError("Input must be a list.")
    try:
        return len([item for item in items])
    except Exception as e:
        raise RuntimeError(f"Error processing input: {e}")
if __name__ == '__main__':
    sample_data = [1, 2, "three", True]
    result = count_top_level_items(sample_data)
    print(result)