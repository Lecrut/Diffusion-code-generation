def sort_descending(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numeric")
    return (max(a, b), min(a, b))

if __name__ == '__main__':
    print(sort_descending(3, 1))
    print(sort_descending(5.5, 2.1))
    print(sort_descending(-1, 0))