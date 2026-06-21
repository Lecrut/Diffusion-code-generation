def key_exists(dict_list, target_key):
    key_set = set(item.keys() for item in dict_list)
    return target_key in key_set

if __name__ == '__main__':
    list1 = [{'a': 1}, {'b': 2}, {'c': 3}]
    key1 = 'b'
    result1 = key_exists(list1, key1)
    print(f"List: {list1}, Key: {key1}, Exists: {result1}")
    
    list2 = [{'x': 5}, {'y': 6}, {'z': 7}]
    key2 = 'w'
    result2 = key_exists(list2, key2)
    print(f"List: {list2}, Key: {key2}, Exists: {result2}")