def sort_descending(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numeric types")
    if a > b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    print(sort_descending(5, 3))
    print(sort_descending(10, 20))
    print(sort_descending(4.5, 4.5))
    print(sort_descending(-1, 0))