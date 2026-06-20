NUM1 = 10
NUM2 = 5

def compute_operations(a, b):
    return a + b, a - b

if __name__ == '__main__':
    sum_result, diff_result = compute_operations(NUM1, NUM2)
    print(sum_result)
    print(diff_result)