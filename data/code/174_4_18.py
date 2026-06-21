def filter_dict_by_value(input_dict, threshold):
    return {key: value for key, value in input_dict.items() if value > threshold}

if __name__ == '__main__':
    sample_dict = {'apple': 150, 'banana': 30, 'cherry': 20, 'date': 45}
    threshold_value = 25
    filtered_fruits = filter_dict_by_value(sample_dict, threshold_value)
    print(filtered_fruits)