def compare_three_numbers(a, b, c):
    try:
        if a > b and b > c:
            print(f"{a} is greater than {b}, and {b} is greater than {c}.")
        elif a < b and b < c:
            print(f"{a} is less than {b}, and {b} is less than {c}.")
        elif a == b == c:
            print(f"{a}, {b}, and {c} are all equal.")
        else:
            print("The relationship between the three numbers is more complex or involves equality among pairs.")
    except TypeError:
        print("Error: All inputs must be numeric values.")
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    num3 = 8
    compare_three_numbers(num1, num2, num3)
    num4 = 20
    num5 = 15
    num6 = 20
    compare_three_numbers(num4, num5, num6)
    num7 = 7
    num8 = 7
    num9 = 7
    compare_three_numbers(num7, num8, num9)
    num10 = 30
    num11 = 20
    num12 = 10
    compare_three_numbers(num10, num11, num12)
    invalid_a = "hello"
    invalid_b = 5
    invalid_c = 10
    compare_three_numbers(invalid_a, invalid_b, invalid_c)