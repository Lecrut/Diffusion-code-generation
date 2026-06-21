def find_max(a: float, b: float, c: float) -> float:
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
if __name__ == '__main__':
    val1 = 3.14
    val2 = 2.71
    val3 = 1.41
    result = find_max(val1, val2, val3)
    print(result)