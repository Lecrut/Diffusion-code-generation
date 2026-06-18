import math
def calculate_series_product(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product
if __name__ == '__main__':
    N = 5
    total_product = calculate_series_product(N)
    result = total_product / N
    print(result)