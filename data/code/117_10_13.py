def calculate_difference(num1, num2):
    return round(num1 - num2, 4)

if __name__ == '__main__':
    value1 = 3.141592653589793
    value2 = 2.718281828459045
    result = calculate_difference(value1, value2)
    print(result)