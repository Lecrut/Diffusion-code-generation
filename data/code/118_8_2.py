def multiply_bitwise(a, b):
    result = 0
    while b > 0:
        if b & 1:
            result = result + a
        a = a << 1
        b = b >> 1
    return result
if __name__ == '__main__':
    num1 = 12
    num2 = 18
    product = multiply_bitwise(num1, num2)
    print(product)