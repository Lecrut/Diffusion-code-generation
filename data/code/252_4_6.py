def compare_and_difference(a, b):
    difference = a - b
    return difference
if __name__ == '__main__':
    num1 = 0.1 + 0.2
    num2 = 0.3
    result1 = compare_and_difference(num1, num2)
    print(f"{result1=}")
    num3 = 1.0
    num4 = 0.9999999999999999
    result2 = compare_and_difference(num3, num4)
    print(f"{result2=}")
    num5 = 1.0 / 3.0
    num6 = 0.3333333333333333
    result3 = compare_and_difference(num5, num6)
    print(f"{result3=}")