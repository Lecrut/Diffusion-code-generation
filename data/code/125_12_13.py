A = 10
B = 5

def compute_operations(a=A, b=B):
    return (a + b, a - b)
if __name__ == '__main__':
    sum_result, diff_result = compute_operations()
    print(f'Sum: {sum_result}, Difference: {diff_result}')