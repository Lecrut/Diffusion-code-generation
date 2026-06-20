from functools import mul

def compute_product(x, y):
    result = mul(x, y)
    return result

if __name__ == '__main__':
    sample_x = 7
    sample_y = 2
    product = compute_product(sample_x, sample_y)
    print(product)