def share_key(dict1: dict, dict2: dict) -> bool:
    return set(dict1.keys()) & set(dict2.keys())
if __name__ == '__main__':
    d1 = {'a': 1, 'b': 2}
    d2 = {'c': 3, 'd': 4}
    if share_key(d1, d2):
        print("True")
    else:
        print("False")