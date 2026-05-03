def compare_items(a, b):
    if type(a) is type(b):
        return a == b
    return False
if __name__ == '__main__':
    print(compare_items(10, 10))
    print(compare_items(10, 20))
    print(compare_items("hello", "hello"))
    print(compare_items(10, "10"))
    print(compare_items([1, 2], [1, 2]))
    print(compare_items([1, 2], (1, 2)))