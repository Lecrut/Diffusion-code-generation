import math
def divide_large_integers(a, b):
    result = float(a) / b
    return result
if __name__ == '__main__':
    num1 = 1234567890123456789
    num2 = 9876543210987654321
    division_result = divide_large_integers(num1, num2)
    print(division_result)