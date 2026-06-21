def find_largest(a: float, b: float, c: float) -> float:
    return a if a > b and a > c else (b if b > c else c)

if __name__ == '__main__':
    val_a = 10.5
    val_b = 20.1
    val_c = 15.3
    result = find_largest(val_a, val_b, val_c)
    print(result)