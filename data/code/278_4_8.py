sample_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

def print_dict_pairs(dictionary):
    for key, value in dictionary.items():
        print(f'{key}: {value}')

if __name__ == '__main__':
    print_dict_pairs(sample_dict)