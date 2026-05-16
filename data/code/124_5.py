def arithmetic_operations(a, b, c):
    sum_val = a + b + c
    product_val = a * b * c
    division_floor = int(a / b / c)
    return (sum_val, product_val, int(a / b))
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    num3 = 2
    result = arithmetic_operations(num1, num2, num3)
    print(result)