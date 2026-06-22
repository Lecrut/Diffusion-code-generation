def print_first_value(d):
    for key in d:
        print(d[key])
        break

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print_first_value(sample_dict)