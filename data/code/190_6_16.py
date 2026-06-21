class KeyVerifier:
    @staticmethod
    def key_exists(key_list, target_key):
        key_set = set(key_list)
        return target_key in key_set

if __name__ == '__main__':
    sample_dict_list = [
        {'a': 1, 'b': 2},
        {'c': 3, 'd': 4},
        {'e': 5, 'f': 6}
    ]
    target_key = 'c'
    result1 = KeyVerifier.key_exists([item.keys() for item in sample_dict_list], target_key)
    print(f"Sample List: {sample_dict_list}, Target Key: {target_key}, Exists: {result1}")

    target_key = 'g'
    result2 = KeyVerifier.key_exists([item.keys() for item in sample_dict_list], target_key)
    print(f"Sample List: {sample_dict_list}, Target Key: {target_key}, Exists: {result2}")