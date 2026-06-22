SAMPLE_DICT = {'name': 'Alice', 'age': 25, 'city': 'Wonderland'}

def print_dict_pairs(dictionary):
    for key, value in dictionary.items():
        print(f'{key}: {value}')

if __name__ == '__main__':
    print_dict_pairs(SAMPLE_DICT)