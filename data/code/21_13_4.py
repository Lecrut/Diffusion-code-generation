def get_max_value(a: float, b: float, c: float) -> float:
    result = a
    if b > result:
        result = b
    if c > result:
        result = c
    return result

if __name__ == '__main__':
    val1 = 3.14
    val2 = 2.71
    val3 = 9.86
    max_val = get_max_value(val1, val2, val3)
    print(max_val)