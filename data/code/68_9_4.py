import numpy as np
def find_zero_difference_index(A, B):
    n = min(len(A), len(B))
    for i in range(n - 1):
        if A[i] - B[i+1] == 0:
            return i
    return -1
if __name__ == '__main__':
    A_sample = [1, 5, 3, 8, 2]
    B_sample = [5, 5, 3, 8, 2]
    result = find_zero_difference_index(A_sample, B_sample)
    print(result)