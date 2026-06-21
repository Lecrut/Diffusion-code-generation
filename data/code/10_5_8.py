def get_first_value(d):
    for value in d.values():
        return value

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print(get_first_value(sample_dict))