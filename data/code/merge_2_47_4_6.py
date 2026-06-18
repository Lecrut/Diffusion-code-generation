def multiply_large_integers(a: int, b: int) -> int:
    return a * b
if __name__ == '__main__':
    num1 = 9223372036854775807
    num2 = -9223372036854775808
    result = multiply_large_integers(num1, num2)
    print(result)