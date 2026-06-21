def sort_descending(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numeric")
    return (a, b) if a >= b else (b, a)

if __name__ == '__main__':
    print(sort_descending(3, 7))
    print(sort_descending(10.5, 2.1))
    print(sort_descending(-5, -1))