def compare_integers(quantity1: int, quantity2: int) -> bool:
    if not isinstance(quantity1, int) or not isinstance(quantity2, int):
        raise ValueError("Both arguments must be integers")
    return quantity1 > quantity2

if __name__ == '__main__':
    result1 = compare_integers(5, 3)
    print(result1)
    result2 = compare_integers(-2, -5)
    print(result2)
    try:
        result3 = compare_integers(0, "a")
        print(result3)
    except ValueError as e:
        print(e)