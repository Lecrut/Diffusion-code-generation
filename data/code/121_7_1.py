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
    result1 = compare_dict_size(dict_a, dict_b)
    print(f"Comparison between dict_a (size {len(dict_a)}) and dict_b (size {len(dict_b)}): {result1}")
    result2 = compare_dict_size(dict_b, dict_a)
    print(f"Comparison between dict_b (size {len(dict_b)}) and dict_a (size {len(dict_a)}): {result2}")
    result3 = compare_dict_size(dict_a, dict_c)
    print(f"Comparison between dict_a (size {len(dict_a)}) and dict_c (size {len(dict_c)}): {result3}")
    result4 = compare_dict_size(dict_c, dict_a)
    print(f"Comparison between dict_c (size {len(dict_c)}) and dict_a (size {len(dict_a)}): {result4}")
    dict_d = {'m': 1}
    dict_e = {'m': 1, 'n': 2}
    result5 = compare_dict_size(dict_d, dict_e)
    print(f"Comparison between dict_d (size {len(dict_d)}) and dict_e (size {len(dict_e)}): {result5}")