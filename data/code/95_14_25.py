def check_conditions(first: float, second: float, third: float) -> bool:
    if first <= 0.0:
        return False
    if second >= first:
        return False
    return abs(third - (first + second)) < 1e-9

if __name__ == '__main__':
    val_a = 10.5
    val_b = 3.2
    val_c = 13.7
    result = check_conditions(val_a, val_b, val_c)
    print(result)