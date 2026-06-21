def is_even(n: int) -> bool:
    if n % 2 == 0:
        return True
    return False

if __name__ == '__main__':
    check_values = [12, 13, 0, -4, -7, 999999999999999998]
    for val in check_values:
        print(is_even(val))