def filter_dict_by_value(input_dict, threshold):
    filtered_dict = {key: value for key, value in input_dict.items() if value >= threshold}
    return filtered_dict

if __name__ == '__main__':
    sample_dict = {
        "apple": 10,
        "banana": 5,
        "cherry": 20,
        "date": 8
    }
    threshold_value = 15
    result_dict = filter_dict_by_value(sample_dict, threshold_value)
    print(f"Original Dictionary: {sample_dict}")
    print(f"Filtered Dictionary: {result_dict}")