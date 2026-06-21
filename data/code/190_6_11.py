def key_exists(key_list, target_key):
    key_set = set(key_list)
    return target_key in key_set

if __name__ == '__main__':
    sample_keys = ['apple', 'banana', 'cherry']
    search_key1 = 'banana'
    result1 = key_exists(sample_keys, search_key1)
    print(f"Keys: {sample_keys}, Key: {search_key1}, Exists: {result1}")

    search_key2 = 'orange'
    result2 = key_exists(sample_keys, search_key2)
    print(f"Keys: {sample_keys}, Key: {search_key2}, Exists: {result2}")