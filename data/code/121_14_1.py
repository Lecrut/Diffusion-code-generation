def compare_numbers(num1, num2):
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num2 > num1:
        print(f"{num2} is greater than {num1}")
    else:
        print(f"{num1} and {num2} are equal")
if __name__ == '__main__':
    a = 42
    b = 99
    compare_numbers(a, b)