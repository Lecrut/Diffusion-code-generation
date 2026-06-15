import math
def calculate_series_and_divide(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    if n != 0:
        result = product / n
        return result
    else:
        return 0
if __name__ == '__main__':
    N = 5
    result = calculate_series_and_divide(N)
    print(result)