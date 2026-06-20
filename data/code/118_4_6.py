from functools import mul

def calculate_product(x, y):
    product = mul(x, y)
    return product

if __name__ == '__main__':
    value_a = 8
    value_b = 3
    result = calculate_product(value_a, value_b)
    print(result)