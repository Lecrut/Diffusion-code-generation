def is_greater_than_ten(value):
    return value > 10

if __name__ == '__main__':
    num1 = 8
    num2 = 15
    result = is_greater_than_ten(num1) or is_greater_than_ten(num2)
    print(result)