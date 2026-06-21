from collections import defaultdict

def get_value(default_dict, key, factory):
    if key not in default_dict:
        default_dict[key] = factory()
    return default_dict[key]

if __name__ == '__main__':
    my_dict = defaultdict(list)
    result = get_value(my_dict, 'key1', list)
    result.append(10)
    result.append(20)
    print(result)
    
    result2 = get_value(my_dict, 'key2', lambda: [1, 2, 3])
    print(result2)
    
    result3 = get_value(my_dict, 'key1', list)
    print(result3)