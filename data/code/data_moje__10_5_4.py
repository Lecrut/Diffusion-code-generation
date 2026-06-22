def print_first_value(d):
    for value in d.values():
        print(value)
        break

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    result = print_first_value(sample_dict)