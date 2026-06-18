def share_key(dict1: dict, dict2: dict) -> bool:
    return set(dict1.keys()) & set(dict2.keys()) != set()
if __name__ == '__main__':
    d_a = {'x': 10, 'y': 20}
    d_b = {'z': 30, 'w': 40}
    print(share_key(d_a, d_b))
    d_c = {'p': 5, 'q': 6}
    d_d = {'r': 7, 's': 8}
    print(share_key(d_c, d_d))
    e1 = {'a': 1}
    e2 = {'b': 2}
    print(share_key(e1, e2))