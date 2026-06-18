def count_top_level_items(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list.")
    return len([item for item in data])
if __name__ == '__main__':
    sample_list = [1, 2, "a", {"key": True}, None]
    result = count_top_level_items(sample_list)
    print(result)