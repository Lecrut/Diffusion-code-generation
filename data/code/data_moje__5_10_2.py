def length_difference(a: float, b: float) -> float:
    return a - b if a >= b else b - a

if __name__ == '__main__':
    print(length_difference(10.5, 3.2))
    print(length_difference(2.1, 9.8))
    print(length_difference(5.0, 5.0))