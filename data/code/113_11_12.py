def subtract_large_numbers(x: int, y: int) -> int:
    return x - y

if __name__ == '__main__':
    num1 = 987654321098765432109876543210
    num2 = 123456789012345678901234567890
    result = subtract_large_numbers(num1, num2)
    print(result)