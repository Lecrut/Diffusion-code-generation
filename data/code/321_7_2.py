import sys
def multiply_large_integers(num1: int, num2: int) -> int:
    return num1 * num2
if __name__ == '__main__':
    a = 1234567890123456789
    b = 9876543210987654321
    result = multiply_large_integers(a, b)
    print(result)