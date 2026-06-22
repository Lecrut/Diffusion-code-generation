def sort_descending(a: float, b: float) -> tuple:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numeric")
    if a > b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    print(sort_descending(3, 7))
    print(sort_descending(10, 2))
    print(sort_descending(5, 5))