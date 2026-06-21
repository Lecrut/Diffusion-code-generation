def find_maximum(a: float, b: float, c: float) -> float:
    max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    return max_val

if __name__ == '__main__':
    val1 = 3.14
    val2 = 2.71
    val3 = 1.41
    result = find_maximum(val1, val2, val3)
    print(result)