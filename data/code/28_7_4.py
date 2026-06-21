def sort_descending(a: float, b: float) -> list:
    if not isinstance(a, (int, float)):
        raise TypeError("First argument must be a number")
    if not isinstance(b, (int, float)):
        raise TypeError("Second argument must be a number")
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Arguments must not be booleans")
    return [a, b] if a >= b else [b, a]

if __name__ == '__main__':
    result1 = sort_descending(3, 7)
    print(result1)
    result2 = sort_descending(10.5, 2.1)
    print(result2)
    result3 = sort_descending(-5, 0)
    print(result3)