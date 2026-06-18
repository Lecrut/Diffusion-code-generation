import math
def large_integer_division(numerator: int, denominator: int) -> float:
    result = numerator / denominator
    return result
if __name__ == '__main__':
    num1 = 1234567890123456789
    num2 = 9876543210987654321
    division_result = large_integer_division(num1, num2)
    print(division_result)