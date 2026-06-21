def evaluate_conditions(x, y, z):
    if x <= 0:
        return False
    if y % 2 != 0:
        return False
    divisor = x * y
    if divisor == 0:
        return False
    return z % divisor == 0

if __name__ == '__main__':
    result = evaluate_conditions(2, 4, 16)
    print(result)