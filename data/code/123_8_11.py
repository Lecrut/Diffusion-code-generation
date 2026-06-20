def sum_numeric_values(input_dict):
    if not isinstance(input_dict, dict):
        raise ValueError("Input must be a dictionary")
    
    numeric_values = (value for value in input_dict.values() if isinstance(value, (int, float)))
    return sum(numeric_values)

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20.5, 'c': 'hello', 'd': 30}
    print(sum_numeric_values(sample_dict))