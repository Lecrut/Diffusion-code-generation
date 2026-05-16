import math
def compare_floats(a, b, epsilon=1e-9):
    if abs(a - b) < epsilon:
        return "Equal"
    elif a > b:
        return "a is larger"
    else:
        return "b is larger"
if __name__ == '__main__':
    num1 = 1.0000000000000001
    num2 = 1.0
    epsilon_val = 1e-12
    result = compare_floats(num1, num2, epsilon_val)
    print(f"Comparing {num1} and {num2}: {result}")
    num3 = 3.14159
    num4 = 3.141590000000001
    result2 = compare_floats(num3, num4, epsilon_val)
    print(f"Comparing {num3} and {num4}: {result2}")
    num5 = 5.0
    num6 = 5.000000000000001
    result3 = compare_floats(num5, num6, epsilon_val)
    print(f"Comparing {num5} and {num6}: {result3}")