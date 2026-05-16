def find_zero_difference_index(A, B):
    n = min(len(A), len(B))
    for i in range(n - 1):
        if A[i] - B[i+1] == 0:
            return i
    return -1
if __name__ == '__main__':
    A_sample = [1, 5, 3, 8, 2]
    B_sample = [1, 5, 3, 8, 2]
    result1 = find_zero_difference_index(A_sample, B_sample)
    print(result1)
    A_sample_2 = [10, 20, 30, 40]
    B_sample_2 = [10, 20, 30, 40]
    result2 = find_zero_difference_index(A_sample_2, B_sample_2)
    print(result2)
    A_sample_3 = [1, 2, 3, 4]
    B_sample_3 = [1, 3, 5, 4]
    result3 = find_zero_difference_index(A_sample_3, B_sample_3)
    print(result3)
    A_sample_4 = [1, 2, 3]
    B_sample_4 = [1, 2, 4]
    result4 = find_zero_difference_index(A_sample_4, B_sample_4)
    print(result4)