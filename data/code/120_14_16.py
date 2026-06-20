def fast_compare(a, b):
    if a is b:
        return True
    if type(a) != type(b):
        return False
    return a == b

if __name__ == '__main__':
    print(fast_compare(10, 10))
    print(fast_compare('hello', 'hello'))
    print(fast_compare([1, 2], [1, 2]))
    print(fast_compare({'a': 1}, {'a': 1}))
    print(fast_compare(None, None))
    print(fast_compare(10, '10'))