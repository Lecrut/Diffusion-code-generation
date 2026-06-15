def compare_three_numbers(a, b, c):
    try:
        if a > b and b > c:
            print(f"{a} is greater than {b}, and {b} is greater than {c}.")
        elif a < b and b < c:
            print(f"{a} is less than {b}, and {b} is less than {c}.")
        elif a == b == c:
            print(f"{a}, {b}, and {c} are all equal.")
        else:
            print("The relationship between the three numbers is more complex or involves mixed comparisons.")
    except TypeError:
        print("Error: All inputs must be numeric values.")
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    num3 = 15
    compare_three_numbers(num1, num2, num3)
    num4 = 20
    num5 = 20
    num6 = 20
    compare_three_numbers(num4, num5, num6)
    num7 = 3
    num8 = 1
    num9 = 5
    compare_three_numbers(num7, num8, num9)
    try:
        compare_three_numbers(10, "a", 5)
    except Exception as e:
        print(f"Caught exception during test: {e}")