import math
def divide_large_integers(a: int, b: int) -> float:
    result = a / b
    return result
if __name__ == '__main__':
    num1 = 123456789012345
    num2 = 543210987654321
    division_result = divide_large_integers(num1, num2)
    print(division_result)