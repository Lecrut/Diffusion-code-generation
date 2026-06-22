def compare_items(a, b):
    if type(a) is not type(b):
        return False
    return a == b
if __name__ == '__main__':
    print(compare_items(10, 20))
    print(compare_items(3.14, 3.14))
    print(compare_items('hello', 'world'))
    print(compare_items([1, 2], [1, 2]))
    print(compare_items((1, 2), (1, 2)))
    print(compare_items({1, 2}, {1, 2}))
    print(compare_items({'a': 1}, {'a': 1}))