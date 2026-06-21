VALID_KEY = 'b'
SAMPLE_DICTS = [{'a': 1}, {'b': 2}, {'c': 3}]

def validate_key_exists(key, dict_list):
    return any(key in d for d in dict_list)

if __name__ == '__main__':
    result = validate_key_exists(VALID_KEY, SAMPLE_DICTS)
    print(result)