def safe_key_check(data: dict, key) -> bool:
    return key in data
if __name__ == '__main__':
    flat_dict = {'a': 1, 'b': 2}
    deep_dict = {
        'x': [1],
        'y': {
            'z': 'found',
            'w': None
        }
    }
    result_flat = safe_key_check(flat_dict, 'c')
    result_deep = safe_key_check(deep_dict, 'z')
    print(result_flat)         
    print(result_deep)