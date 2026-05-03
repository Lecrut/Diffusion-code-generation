def compare_values(v1, v2):
    return v1 == v2
if __name__ == '__main__':
    print(compare_values(5, 5))
    print(compare_values(10, 10))
    print(compare_values(3.14, 3.14))
    print(compare_values(1, 2))
    print(compare_values("hello", "hello"))
    print(compare_values(100, 99))