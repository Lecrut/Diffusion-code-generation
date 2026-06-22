sample_dict = {'a': 1, 'b': 2, 'c': 3}

def print_key_value_pairs(dictionary):
    for key, value in dictionary.items():
        print(f'{key}: {value}')

if __name__ == '__main__':
    print_key_value_pairs(sample_dict)