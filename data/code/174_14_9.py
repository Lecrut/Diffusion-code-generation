def filter_dict_by_value(input_dict, threshold):
    return {key: value for key, value in input_dict.items() if value >= threshold}

if __name__ == '__main__':
    sample_dict = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "David": 95
    }
    threshold_value = 90
    filtered_dict = filter_dict_by_value(sample_dict, threshold_value)
    print(f"Filtered Dictionary: {filtered_dict}")