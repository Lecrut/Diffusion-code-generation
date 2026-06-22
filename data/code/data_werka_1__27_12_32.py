def values_differ(a, b):
    return a != b
if __name__ == '__main__':
    result = values_differ(10, 20)
    print(result)
    result = values_differ('hello', 'hello')
    print(result)
    result = values_differ([1, 2], [1, 2])
    print(result)
    result = values_differ({'a': 1}, {'a': 1})
    print(result)