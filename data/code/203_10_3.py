import math
def compare_floats(a, b, epsilon=1e-9):
    if abs(a - b) < epsilon:
        print(f"{a} and {b} are considered equal.")
    elif a > b:
        print(f"{a} is larger than {b}.")
    else:
        print(f"{b} is larger than {a}.")
if __name__ == '__main__':
    num1 = 1.0 / 3.0
    num2 = 0.3333333333333333
    compare_floats(num1, num2)
    num3 = 1.0000000000000001
    num4 = 1.0
    compare_floats(num3, num4)
    num5 = 5.000000000000001
    num6 = 5.0
    compare_floats(num5, num6)