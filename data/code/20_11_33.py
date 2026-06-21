def compare_items(a, b):
    if type(a) is not type(b):
        return False
    return a == b
if __name__ == '__main__':
    print(compare_items(10, 10))
    print(compare_items('hello', 'hello'))
    print(compare_items([1, 2], [1, 2]))
    print(compare_items(10, '10'))
    print(compare_items('hello', 10))