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
        print("Error: One or more inputs provided were not valid numbers.")
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    num3 = 15
    compare_three_numbers(num1, num2, num3)
    print("-" * 20)
    num4 = 7
    num5 = 7
    num6 = 7
    compare_three_numbers(num4, num5, num6)
    print("-" * 20)
    num7 = 20
    num8 = 10
    num9 = 5
    compare_three_numbers(num7, num8, num9)
    print("-" * 20)
    num10 = "a"
    num11 = 5
    num12 = 10
    compare_three_numbers(num10, num11, num12)