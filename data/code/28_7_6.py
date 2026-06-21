def sort_descending(a: float, b: float) -> list:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numeric")
    return sorted([a, b], reverse=True)

if __name__ == '__main__':
    print(sort_descending(5, 3))
    print(sort_descending(10.5, 2.1))
    print(sort_descending(-1, -10))