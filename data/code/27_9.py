def compare_numbers(a, b):
    if a > b:
        return "a is greater than b"
    elif a < b:
        return "a is less than b"
    else:
        return "a is equal to b"
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    print(compare_numbers(num1, num2))
    num3 = 20
    num4 = 20
    print(compare_numbers(num3, num4))
    num5 = 3.14159
    num6 = 3.1415900000000004
    print(compare_numbers(num5, num6))