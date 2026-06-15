def compare_numbers(a, b):
    if a > b:
        print(f"{a} is larger than {b}")
    elif b > a:
        print(f"{b} is larger than {a}")
    else:
        print(f"{a} and {b} are equal")
if __name__ == '__main__':
    num1 = 42
    num2 = 99
    compare_numbers(num1, num2)