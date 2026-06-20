def sum_dict_values(input_dict):
    return sum(value for value in input_dict.values() if isinstance(value, (int, float)))

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20.5, 'c': 'not a number', 'd': 30}
    print(sum_dict_values(sample_dict))