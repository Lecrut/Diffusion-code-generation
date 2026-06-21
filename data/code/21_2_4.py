def find_largest(a: float, b: float, c: float) -> float:
    return a if a >= b and a >= c else (b if b >= c else c)

if __name__ == '__main__':
    val1 = 10
    val2 = 25
    val3 = 15
    print(find_largest(val1, val2, val3))