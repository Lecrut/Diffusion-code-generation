def find_zero_difference_index(A, B):
    n = min(len(A), len(B))
    for i in range(n - 1):
        if A[i] - B[i+1] == 0:
            return i
    return -1
if __name__ == '__main__':
    A_sample = [1, 5, 3, 8, 2]
    B_sample = [5, 5, 3, 10, 2]
    result = find_zero_difference_index(A_sample, B_sample)
    print(result)
    A_sample_2 = [10, 20, 30, 40]
    B_sample_2 = [10, 20, 30, 40]
    result_2 = find_zero_difference_index(A_sample_2, B_sample_2)
    print(result_2)
    A_sample_3 = [1, 2, 3]
    B_sample_3 = [1, 3, 5]
    result_3 = find_zero_difference_index(A_sample_3, B_sample_3)
    print(result_3)
    A_sample_4 = [1, 1, 5, 3]
    B_sample_4 = [1, 1, 3, 3]
    result_4 = find_zero_difference_index(A_sample_4, B_sample_4)
    print(result_4)