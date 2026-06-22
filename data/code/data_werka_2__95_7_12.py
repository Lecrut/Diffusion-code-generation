def check_conditions(a, b, c):
    if a <= 0:
        return False
    if b % 2 != 0:
        return False
    product = a * b
    if product == 0:
        return False
    return c % product == 0

if __name__ == '__main__':
    result = check_conditions(2, 4, 8)
    print(result)