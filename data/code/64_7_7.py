def power(base: float, exponent: float) -> float:
    return base ** exponent

if __name__ == '__main__':
    print(power(2, 3))
    print(power(4, 0.5))
    print(power(9, 0.5))
    print(power(2, -1))
    print(power(0, 5))
    print(power(5, 0))