def compare_data(a, b):
    if type(a) != type(b):
        return a == b
    else:
        return a == b
if __name__ == '__main__':
    print(compare_data(10, 10))
    print(compare_data(10.0, 10))
    print(compare_data(10, 10.0))
    print(compare_data("hello", "hello"))
    print(compare_data("hello", "world"))
    print(compare_data(3.14, 3.1400000000000004))
    print(compare_data([1], [1]))
    print(compare_data(None, None))
    print(compare_data(5, 6))