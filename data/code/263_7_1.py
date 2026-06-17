def compare_and_report(a, b):
    if a > b:
        print(f"The first integer ({a}) is greater than the second integer ({b}).")
    elif a < b:
        print(f"The first integer ({a}) is less than the second integer ({b}).")
    else:
        print(f"The first integer ({a}) is equal to the second integer ({b}).")
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    compare_and_report(num1, num2)
    num3 = 20
    num4 = 20
    compare_and_report(num3, num4)
    num5 = 3
    num6 = 15
    compare_and_report(num5, num6)