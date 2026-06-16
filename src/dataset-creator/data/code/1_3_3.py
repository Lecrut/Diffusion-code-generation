def has_common_key(dict1: dict, dict2: dict) -> bool:
    return set(dict1.keys()) & set(dict2.keys()) != set()
if __name__ == '__main__':
    d_a = {'x': 10, 'y': 20}
    d_b = {'p': 30, 'q': 40}
    print(has_common_key(d_a, d_b))
    d_c = {'m': 5, 'n': 6}
    d_d = {'x': 100, 'o': 7}
    print(has_common_key(d_c, d_d))