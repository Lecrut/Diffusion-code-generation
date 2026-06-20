def check_numbers(num1, num2):
    return num1 + num2 > abs(num1 - num2)

if __name__ == '__main__':
    print(check_numbers(5, 3))