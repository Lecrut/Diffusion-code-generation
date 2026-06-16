def count_top_level_items(items):
    if not isinstance(items, list):
        raise TypeError("Input must be a list.")
    return len([item for item in items])
if __name__ == '__main__':
    sample_data = [1, 2, "apple", {"key": "value"}, None]
    result = count_top_level_items(sample_data)
    print(result)