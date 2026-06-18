def calculate_series_product_and_divide(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    result = product / n
    return result
if __name__ == '__main__':
    N = 5
    result = calculate_series_product_and_divide(N)
    print(result)