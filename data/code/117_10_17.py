def calculate_difference(num1, num2):
    return round(num1 - num2, 4)

if __name__ == '__main__':
    num1 = 15.0001
    num2 = 7.9999
    result = calculate_difference(num1, num2)
    print(result)