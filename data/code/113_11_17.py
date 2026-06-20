def subtract_large_integers(a: int, b: int) -> int:
    result = a - b
    return result

if __name__ == '__main__':
    x = 123456789012345678901234567890
    y = 987654321098765432109876543210
    result = subtract_large_integers(x, y)
    print(result)