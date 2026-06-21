def sort_descending(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numeric")
    if a >= b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    print(sort_descending(3, 7))
    print(sort_descending(10, 2))
    print(sort_descending(5.5, 5.5))
    print(sort_descending(-1, 4))