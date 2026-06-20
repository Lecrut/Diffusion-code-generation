def multiply_large_integers(a, b):
    return a * b

if __name__ == '__main__':
    num1 = 12345678901234567890
    num2 = 98765432109876543210
    result = multiply_large_integers(num1, num2)
    print(result)