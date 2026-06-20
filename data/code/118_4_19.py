from functools import mul

def multiply_numbers(x, y):
    product = mul(x, y)
    return product

if __name__ == '__main__':
    sample_num1 = 8
    sample_num2 = 9
    result = multiply_numbers(sample_num1, sample_num2)
    print(result)