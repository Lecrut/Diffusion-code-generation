def add_decimals(a, b):
    return round(a + b, 10)

if __name__ == '__main__':
    num1 = 3.1415926536
    num2 = 2.7182818284
    result = add_decimals(num1, num2)
    print(result)