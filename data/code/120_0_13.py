def are_values_equal(a: any, b: any) -> bool:
    if not isinstance(a, type(b)):
        return False
    return a == b

if __name__ == '__main__':
    print(are_values_equal(5, 5))
    print(are_values_equal("hello", "hello"))
    print(are_values_equal([1, 2], [1, 2]))
    print(are_values_equal(3.14, 3.1400000000000004))