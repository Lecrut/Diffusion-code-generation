import math
def large_integer_division(numerator, denominator):
    result = numerator / denominator
    return result
if __name__ == '__main__':
    num1 = 1234567890123456789
    num2 = 3141592653589793238
    division_result = large_integer_division(num1, num2)
    print(division_result)