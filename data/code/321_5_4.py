import math
def precise_product(a: float, b: float) -> float:
    return a * b
if __name__ == '__main__':
    num1 = 0.1
    num2 = 0.2
    result = precise_product(num1, num2)
    print(result)
    num3 = 1.0
    num4 = 5.0
    result2 = precise_product(num3, num4)
    print(result2)
    num5 = -3.14159
    num6 = 2.0
    result3 = precise_product(num5, num6)
    print(result3)