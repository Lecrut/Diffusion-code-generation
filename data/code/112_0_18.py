num_dict = {'a': 15, 'b': 27}

def add_numbers(num_map):
    return num_map['a'] + num_map['b']

if __name__ == '__main__':
    result = add_numbers(num_dict)
    print(result)