def arithmetic_operations(a, b, c):
    sum_val = a + b + c
    product_val = a * b * c
    floor_division = a // b if b != 0 else 0
    return (sum_val, product_val, floor_division)
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    num3 = 3
    result = arithmetic_operations(num1, num2, num3)
    print(result)