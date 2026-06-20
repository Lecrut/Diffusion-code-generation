def calculate_difference(num1, num2):
    return round(num1 - num2, 4)

if __name__ == '__main__':
    num1 = 15.3456789
    num2 = 7.1234567
    difference = calculate_difference(num1, num2)
    print(difference)