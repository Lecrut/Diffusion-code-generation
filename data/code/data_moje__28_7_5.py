def sort_numbers_descending(a: float, b: float) -> tuple:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numeric")
    if a >= b:
        return (a, b)
    return (b, a)

if __name__ == '__main__':
    result = sort_numbers_descending(5, 10)
    print(result)