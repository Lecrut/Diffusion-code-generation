def compare_values(a, b):
    if type(a) is type(b):
        return a == b
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a == b
    elif isinstance(a, str) and isinstance(b, str):
        return a == b
    else:
        try:
            return a == b
        except Exception:
            return False
if __name__ == '__main__':
    print(compare_values(10, 10))
    print(compare_values(10.0, 10))
    print(compare_values(10, 10.0))
    print(compare_values("hello", "hello"))
    print(compare_values("hello", "world"))
    print(compare_values(3.14, 3.1400000000000004))
    print(compare_values([1], [1]))
    print(compare_values(None, None))
    print(compare_values(1, "1"))