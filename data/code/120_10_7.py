def safe_compare(a, b):
    if type(a) is not type(b):
        return False
    return a is b
if __name__ == '__main__':
    print(safe_compare(1, 1))
    print(safe_compare(1, 2))
    print(safe_compare('hello', 'hello'))
    print(safe_compare('hello', 'world'))
    print(safe_compare([1, 2], [1, 2]))
    print(safe_compare([1, 2], (1, 2)))