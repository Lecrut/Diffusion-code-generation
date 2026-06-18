def has_key(d: dict, key) -> bool:
    return key in d
if __name__ == '__main__':
    data = {'apple': 1, 'banana': 2}
    if has_key(data, 'banana'):
        print("Key found")
    else:
        print("Key missing")