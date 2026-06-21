def values_differ(a, b):
    return a != b
if __name__ == '__main__':
    print(values_differ(10, 20))
    print(values_differ('hello', 'hello'))
    print(values_differ([1, 2], [1, 2]))
    print(values_differ({'a': 1}, {'a': 1}))
    print(values_differ(3.14, 3.14))