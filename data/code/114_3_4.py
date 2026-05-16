import math
def robust_product(a: float, b: float) -> float:
    return a * b
if __name__ == '__main__':
    num1 = 0.1
    num2 = 0.2
    result = robust_product(num1, num2)
    print(result)
    num3 = 1.0 / 3.0
    num4 = 0.3333333333333333
    result2 = robust_product(num3, num4)
    print(result2)
    num5 = 1.0
    num6 = 1.0
    result3 = robust_product(num5, num6)
    print(result3)