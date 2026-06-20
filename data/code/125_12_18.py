def compute_operations(a=5, b=3):
    return a + b, a - b

if __name__ == '__main__':
    sum_result, diff_result = compute_operations()
    print(sum_result)
    print(diff_result)