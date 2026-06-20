DECIMAL_PRECISION = 28

def multiply_decimals(a, b):
    return round(a * b, DECIMAL_PRECISION)

if __name__ == '__main__':
    result = multiply_decimals(0.1, 0.2)
    print(result)