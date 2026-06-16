def has_common_key(dict1: dict, dict2: dict) -> bool:
    return len(set(dict1.keys()) & set(dict2.keys())) > 0
if __name__ == '__main__':
    d_a = {'x': 1, 'y': 2}
    d_b = {'z': 3, 'w': 4}
    print(has_common_key(d_a, d_b))
    d_c = {'p': 5, 'q': 6}
    d_d = {'r': 7, 'x': 8}
    print(has_common_key(d_c, d_d))