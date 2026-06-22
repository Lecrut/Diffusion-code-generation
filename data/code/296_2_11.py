def are_proportional(num1, num2, num3):
    if num2 == 0 or num3 == 0:
        raise ValueError("Cannot calculate ratio when any of the numbers is zero")
    return num1 * num3 == num2 * num2

if __name__ == '__main__':
    a = 9
    b = 6
    c = 4
    print(f"Are {a}, {b}, and {c} proportional? {are_proportional(a, b, c)}")