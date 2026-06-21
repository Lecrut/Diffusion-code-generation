def print_first_value(data_dict):
    for value in data_dict.values():
        print(value)
        break

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print_first_value(sample_dict)