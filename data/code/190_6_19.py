def key_exists(key_list, search_key):
    key_set = set(key_list)
    return search_key in key_set

if __name__ == '__main__':
    sample_keys = ['apple', 'banana', 'cherry']
    search_key1 = 'banana'
    print(f"Key: {search_key1}, Exists: {key_exists(sample_keys, search_key1)}")
    
    search_key2 = 'grape'
    print(f"Key: {search_key2}, Exists: {key_exists(sample_keys, search_key2)}")