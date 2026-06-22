def sum_digits_recursive(n):
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + sum_digits_recursive(n // 10)

def sum_digits_optimized(n):
    n = abs(n)
    def helper(current):
        if current < 10:
            return current
        return current % 10 + helper(current // 10)
    return helper(n)

if __name__ == '__main__':
    sample_values = [0, 5, 123, 987654321, -456]
    for val in sample_values:
        result_direct = sum_digits_recursive(val)
        result_optimized = sum_digits_optimized(val)
        print(f"{val}: {result_direct}, {result_optimized}")