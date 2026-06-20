def safe_compare(a, b):
    if type(a) is not type(b):
        return False
    if a is b:
        return True
    try:
        return a == b
    except Exception:
        return False
if __name__ == '__main__':
    print(safe_compare(1, 1))
    print(safe_compare(1, '1'))
    print(safe_compare([1], [1]))
    print(safe_compare([1], [2]))