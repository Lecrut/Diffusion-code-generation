def print_first_value(data):
    for value in data.values():
        print(value)
        break

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print_first_value(sample_dict)