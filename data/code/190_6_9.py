def key_exists(key_list, search_key):
    key_set = set(key_list)
    return search_key in key_set

if __name__ == '__main__':
    sample_keys = ['apple', 'banana', 'cherry']
    search_for = 'banana'
    print(key_exists(sample_keys, search_for))