def multiply_integers(a: int, b: int) -> int:
    if type(a) != int or type(b) != int:
        raise TypeError("Both arguments must be integers.")
    return a * b
if __name__ == '__main__':
    result = multiply_integers(4, 5)
    print(result)