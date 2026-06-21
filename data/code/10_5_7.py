def print_first_value(d):
    keys = list(d.keys())
    if keys:
        print(d[keys[0]])

if __name__ == '__main__':
    sample_data = {'a': 1, 'b': 2, 'c': 3}
    print_first_value(sample_data)