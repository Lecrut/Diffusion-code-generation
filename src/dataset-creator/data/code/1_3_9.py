def share_key(dict1: dict, dict2: dict) -> bool:
    return set(dict1.keys()) & set(dict2.keys()) != set()
if __name__ == '__main__':
    d_a = {'x': 10, 'y': 20}
    d_b = {'z': 30, 'w': 40}
    print(share_key(d_a, d_b))
    c_x = {'p': 5, 'q': 6}
    c_y = {'r': 7, 's': 8}
    print(not share_key(c_x, c_y))