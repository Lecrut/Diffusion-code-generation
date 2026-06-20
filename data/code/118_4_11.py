from functools import mul

def calculate_product(x, y):
    return mul(x, y)

if __name__ == '__main__':
    sample_x = 8
    sample_y = 3
    product = calculate_product(sample_x, sample_y)
    print(product)