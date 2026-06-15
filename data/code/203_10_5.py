import math
def compare_floats(a, b, epsilon=1e-9):
    if abs(a - b) < epsilon:
        return "Equal"
    elif a > b:
        return "a is larger"
    else:
        return "b is larger"
if __name__ == '__main__':
    num1 = 1.0 / 3.0
    num2 = 0.3333333333333333
    epsilon_val = 1e-12
    result = compare_floats(num1, num2, epsilon_val)
    print(f"Comparing {num1} and {num2}:")
    print(result)