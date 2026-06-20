from functools import mul

def multiply_numbers(x, y):
    return mul(x, y)

if __name__ == '__main__':
    num1 = 9
    num2 = 8
    product_result = multiply_numbers(num1, num2)
    print(product_result)