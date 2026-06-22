def print_dict_pairs(dictionary):
    for key, value in dictionary.items():
        print(f'{key}: {value}')

if __name__ == '__main__':
    SAMPLE_DICT = {
        'id': 123,
        'name': 'Qwen',
        'version': '1.0'
    }
    print_dict_pairs(SAMPLE_DICT)