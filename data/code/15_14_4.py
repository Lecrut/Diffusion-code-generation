def compare_values(v1, v2):
    return v1 == v2
if __name__ == '__main__':
    print(compare_values(5, 5))
    print(compare_values(10, 5))
    print(compare_values("hello", "hello"))
    print(compare_values(3.14, 3.1400000000000004))