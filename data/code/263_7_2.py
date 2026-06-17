def compare_and_report(a, b):
    if a > b:
        print(f"{a} is greater than {b}.")
    elif a < b:
        print(f"{a} is less than {b}.")
    else:
        print(f"{a} is equal to {b}.")
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    compare_and_report(num1, num2)
    num1 = 7
    num2 = 7
    compare_and_report(num1, num2)
    num1 = 3
    num2 = 12
    compare_and_report(num1, num2)