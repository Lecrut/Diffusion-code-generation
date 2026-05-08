import operator
def compare_by_size(dict1, dict2):
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
    result1 = compare_by_size(dict_a, dict_b)
    print(f"Comparison between dict_a (size {len(dict_a)}) and dict_b (size {len(dict_b)}): {result1}")
    result2 = compare_by_size(dict_c, dict_d)
    print(f"Comparison between dict_c (size {len(dict_c)}) and dict_d (size {len(dict_d)}): {result2}")
    result3 = compare_by_size(dict_a, dict_c)
    print(f"Comparison between dict_a (size {len(dict_a)}) and dict_c (size {len(dict_c)}): {result3}")
    result4 = compare_by_size(dict_b, dict_d)
    print(f"Comparison between dict_b (size {len(dict_b)}) and dict_d (size {len(dict_d)}): {result4}")
    result5 = compare_by_size(dict_a, dict_a)
    print(f"Comparison between dict_a (size {len(dict_a)}) and dict_a (size {len(dict_a)}): {result5}")