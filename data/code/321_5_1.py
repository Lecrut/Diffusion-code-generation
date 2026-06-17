import math
def precise_product(a: float, b: float) -> float:
    return a * b
if __name__ == '__main__':
    num1 = 0.1
    num2 = 0.2
    result = precise_product(num1, num2)
    print(result)
    num3 = 1.0 / 3.0
    num4 = 0.3
    result2 = precise_product(num3, num4)
    print(result2)