def compare_numbers(a, b):
    if a > b:
        return f"{a} is larger than {b}"
    elif a < b:
        return f"{a} is smaller than {b}"
    else:
        return f"{a} and {b} are equal"
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    print(compare_numbers(num1, num2))
    num3 = 20
    num4 = 20
    print(compare_numbers(num3, num4))
    num5 = 3
    num6 = 15
    print(compare_numbers(num5, num6))