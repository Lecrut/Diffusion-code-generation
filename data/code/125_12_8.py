def compute_operations(a, b):
    return a + b, a - b

if __name__ == '__main__':
    result_sum, result_diff = compute_operations(10, 5)
    print(result_sum)
    print(result_diff)