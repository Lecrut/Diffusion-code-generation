def key_exists_in_dict_list(dict_list, key):
    keys_set = {item for d in dict_list if isinstance(d, dict) for item in d}
    return key in keys_set

if __name__ == '__main__':
    list1 = [{'a': 1}, {'b': 2}, {'c': 3}]
    key1 = 'b'
    result1 = key_exists_in_dict_list(list1, key1)
    print(f"List: {list1}, Key: {key1}, Exists: {result1}")

    list2 = [{'x': 5}, {'y': 10}, {'z': 15}]
    key2 = 'w'
    result2 = key_exists_in_dict_list(list2, key2)
    print(f"List: {list2}, Key: {key2}, Exists: {result2}")

    list3 = [{'m': 20}, {'n': 30}, {'o': 40}]
    key3 = 'm'
    result3 = key_exists_in_dict_list(list3, key3)
    print(f"List: {list3}, Key: {key3}, Exists: {result3}")