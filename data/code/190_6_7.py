def key_exists(key_list, target_key):
    key_set = set(key_list)
    return target_key in key_set

if __name__ == '__main__':
    sample_keys = ['apple', 'banana', 'cherry']
    target = 'banana'
    print(key_exists(sample_keys, target))