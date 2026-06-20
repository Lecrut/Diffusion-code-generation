def add_decimals(a, b):
    return round(a + b, 2)

if __name__ == '__main__':
    num1 = 3.14159
    num2 = 2.71828
    result = add_decimals(num1, num2)
    print(result)