def filter_dict_by_value(input_dict, threshold):
    filtered_dict = {key: value for key, value in input_dict.items() if value >= threshold}
    return filtered_dict

if __name__ == '__main__':
    sample_dict = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "David": 95
    }
    threshold = 90
    result = filter_dict_by_value(sample_dict, threshold)
    print(f"Filtered Dictionary: {result}")