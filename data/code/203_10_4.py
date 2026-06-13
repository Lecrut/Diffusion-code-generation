import math
def compare_floats(a, b, epsilon=1e-9):
    if abs(a - b) < epsilon:
        return "Equal"
    elif a > b:
        return "a is larger"
    else:
        return "b is larger"
if __name__ == '__main__':
    num1 = 0.1 + 0.2
    num2 = 0.3
    print(f"Comparing {num1} and {num2}")
    result = compare_floats(num1, num2)
    print(result)
    num3 = 1.0000000000000001
    num4 = 1.0
    print(f"Comparing {num3} and {num4}")
    result = compare_floats(num3, num4)
    print(result)
    num5 = 5.000000000000001
    num6 = 5.0
    print(f"Comparing {num5} and {num6}")
    result = compare_floats(num5, num6)
    print(result)