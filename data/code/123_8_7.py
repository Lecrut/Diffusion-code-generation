def filter_numeric_values(input_dict):
    return {key: value for key, value in input_dict.items() if isinstance(value, (int, float))}

def calculate_sum(filtered_dict):
    return sum(filtered_dict.values())

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20.5, 'c': 'hello', 'd': 30}
    filtered_values = filter_numeric_values(sample_dict)
    result = calculate_sum(filtered_values)
    print(result)