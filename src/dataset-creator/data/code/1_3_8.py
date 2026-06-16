def has_common_key(dict1: dict, dict2: dict) -> bool:
    return set(dict1.keys()) & set(dict2.keys()) != set()
if __name__ == '__main__':
    d_a = {'x': 10, 'y': 20}
    d_b = {'z': 30, 'w': 40}
    print(has_common_key(d_a, d_b))
    d_c = {'p': 5, 'q': 6}
    d_d = {'r': 7, 's': 8, 't': 9}
    print(has_common_key(d_c, d_d))
    e_e = {'m': 1}
    f_f = {'n': 2}
    g_g = {'o': 3}
    h_h = {'p': 4}
    i_i = {'q': 5}