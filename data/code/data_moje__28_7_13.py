def sort_descending(a: float, b: float) -> tuple:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numeric")
    return (max(a, b), min(a, b))

if __name__ == '__main__':
    result = sort_descending(3, 7)
    print(result)
    result = sort_descending(10.5, 2.1)
    print(result)
    result = sort_descending(-1, -5)
    print(result)
    result = sort_descending(0, 0)
    print(result)