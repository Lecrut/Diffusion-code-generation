def fast_compare(a, b):
    return a == b
if __name__ == '__main__':
    print(fast_compare(10, 10))
    print(fast_compare(10, 20))
    print(fast_compare('hello', 'hello'))
    print(fast_compare('hello', 'world'))