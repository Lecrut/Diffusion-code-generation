def filter_dict_by_value(input_dict, threshold):
    if not isinstance(input_dict, dict) or not all(isinstance(value, (int, float)) for value in input_dict.values()):
        raise ValueError("Input must be a dictionary with numeric values")
    
    return {key: value for key, value in input_dict.items() if value > threshold}

if __name__ == '__main__':
    sample_dict = {'apple': 3.50, 'banana': 2.75, 'cherry': 1.00, 'date': 4.00}
    threshold_value = 2.00
    filtered_prices = filter_dict_by_value(sample_dict, threshold_value)
    print(filtered_prices)