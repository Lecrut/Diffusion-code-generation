import operator
def compare_dict_size(dict1, dict2):
    size1 = len(dict1.items())
    size2 = len(dict2.items())
    if size1 > size2:
        return 1
    elif size1 < size2:
        return -1
    else:
        return 0
if __name__ == '__main__':
    dict_a = {'a': 1, 'b': 2, 'c': 3}
    dict_b = {'x': 10, 'y': 20, 'z': 30, 'w': 40}
    dict_c = {'p': 'hello'}
    dict_d = {'q': 'world', 'r': 'test'}
    result1 = compare_dict_size(dict_a, dict_b)
    print(f"Comparing dict_a ({len(dict_a)} items) and dict_b ({len(dict_b)} items): {result1}")
    result2 = compare_dict_size(dict_b, dict_a)
    print(f"Comparing dict_b ({len(dict_b)} items) and dict_a ({len(dict_a)} items): {result2}")
    result3 = compare_dict_size(dict_c, dict_d)
    print(f"Comparing dict_c ({len(dict_c)} items) and dict_d ({len(dict_d)} items): {result3}")
    result4 = compare_dict_size(dict_a, dict_c)
    print(f"Comparing dict_a ({len(dict_a)} items) and dict_c ({len(dict_c)} items): {result4}")
    result5 = compare_dict_size(dict_a, dict_a)
    print(f"Comparing dict_a ({len(dict_a)} items) and dict_a ({len(dict_a)} items): {result5}")