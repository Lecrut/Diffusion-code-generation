def compare_values(a, b):
    return a == b

if __name__ == '__main__':
    print(compare_values(10, 10))
    print(compare_values(10, 20))
    print(compare_values("hello", "hello"))
    print(compare_values("hello", "world"))