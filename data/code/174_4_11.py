def filter_dict_by_value(dictionary, threshold):
    if not isinstance(dictionary, dict) or not all(isinstance(value, (int, float)) for value in dictionary.values()):
        raise ValueError("Invalid input: dictionary must contain only numeric values")
    if not isinstance(threshold, (int, float)):
        raise ValueError("Invalid input: threshold must be a number")

    return {key: value for key, value in dictionary.items() if value > threshold}

if __name__ == '__main__':
    sample_dict = {'apple': 3.50, 'banana': 2.75, 'cherry': 1.00, 'date': 4.00}
    threshold_value = 2.00
    filtered_prices = filter_dict_by_value(sample_dict, threshold_value)
    print(filtered_prices)