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
    dict_c = {'p': 5}
    dict_d = {'q': 6}
    dict_e = {'a': 1, 'b': 2, 'c': 3}
    print(f"Comparing dict_a (size {len(dict_a)}) and dict_b (size {len(dict_b)}): {compare_dict_size(dict_a, dict_b)}")
    print(f"Comparing dict_b (size {len(dict_b)}) and dict_a (size {len(dict_a)}): {compare_dict_size(dict_b, dict_a)}")
    print(f"Comparing dict_c (size {len(dict_c)}) and dict_d (size {len(dict_d)}): {compare_dict_size(dict_c, dict_d)}")
    print(f"Comparing dict_a (size {len(dict_a)}) and dict_e (size {len(dict_e)}): {compare_dict_size(dict_a, dict_e)}")
    print(f"Comparing dict_e (size {len(dict_e)}) and dict_a (size {len(dict_a)}): {compare_dict_size(dict_e, dict_a)}")