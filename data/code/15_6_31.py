if __name__ == '__main__':
    sample_dict = {
        'key1': 42,
        'key2': 42,
        'key3': 99
    }

    keys_to_compare = ['key1', 'key2']
    result_dict = {f'{keys_to_compare[0]}_equals_{keys_to_compare[1]}': sample_dict[keys_to_compare[0]] == sample_dict[keys_to_compare[1]]}

    print(result_dict)