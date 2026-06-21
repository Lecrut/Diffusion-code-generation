def key_exists(key_list, target_key):
    key_set = set(key_list)
    return target_key in key_set

if __name__ == '__main__':
    sample_keys = ['apple', 'banana', 'cherry']
    search_key1 = 'banana'
    result1 = key_exists(sample_keys, search_key1)
    print(f"Keys: {sample_keys}, Search Key: {search_key1}, Exists: {result1}")

    sample_keys = [10, 20, 30, 40, 50]
    search_key2 = 30
    result2 = key_exists(sample_keys, search_key2)
    print(f"Keys: {sample_keys}, Search Key: {search_key2}, Exists: {result2}")

    sample_keys = ['a', 'b', 'c']
    search_key3 = 'd'
    result3 = key_exists(sample_keys, search_key3)
    print(f"Keys: {sample_keys}, Search Key: {search_key3}, Exists: {result3}")