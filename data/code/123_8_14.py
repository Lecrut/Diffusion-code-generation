def sum_numeric_values(dictionary):
    return sum(value for value in dictionary.values() if isinstance(value, (int, float)))

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20.5, 'c': 'hello', 'd': 30}
    print(sum_numeric_values(sample_dict))