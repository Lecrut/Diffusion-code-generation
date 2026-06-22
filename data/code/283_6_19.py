def count_non_dictionaries(data):
    non_dict_count = 0
    for item in data:
        if not isinstance(item, dict):
            non_dict_count += 1
    return non_dict_count

if __name__ == '__main__':
    sample_list = [1, "hello", {"key": "value"}, [], (1, 2), None]
    result = count_non_dictionaries(sample_list)
    print(f"Number of non-dictionary elements: {result}")