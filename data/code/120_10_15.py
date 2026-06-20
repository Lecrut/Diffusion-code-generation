def safe_compare(a, b):
    if type(a) is not type(b):
        return False
    return a is b
if __name__ == '__main__':
    print(safe_compare(1, 1))
    print(safe_compare('a', 'a'))
    print(safe_compare([1], [1]))
    print(safe_compare(None, None))
    print(safe_compare(True, False))