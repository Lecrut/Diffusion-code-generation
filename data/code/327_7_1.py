import math
def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total
def sum_of_squares_optimized(n):
    return n * (n + 1) * (2 * n + 1) // 6
if __name__ == '__main__':
    N = 100
    result_loop = sum_of_squares(N)
    result_optimized = sum_of_squares_optimized(N)
    print(f"N: {N}")
    print(f"Sum of squares (Loop method): {result_loop}")
    print(f"Sum of squares (Optimized method): {result_optimized}")