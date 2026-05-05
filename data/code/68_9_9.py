import collections
def find_first_zero_difference_index(A, B):
    n = min(len(A), len(B))
    for i in range(n - 1):
        if A[i] == B[i + 1]:
            return i
    return -1
if __name__ == '__main__':
    A_sample = [1, 2, 3, 4, 5]
    B_sample = [2, 3, 5, 6, 7]
    result1 = find_first_zero_difference_index(A_sample, B_sample)
    print(result1)
    A_sample_2 = [10, 20, 30, 40]
    B_sample_2 = [20, 30, 40, 50]
    result2 = find_first_zero_difference_index(A_sample_2, B_sample_2)
    print(result2)
    A_sample_3 = [1, 1, 3, 4]
    B_sample_3 = [1, 2, 4, 5]
    result3 = find_first_zero_difference_index(A_sample_3, B_sample_3)
    print(result3)
    A_sample_4 = [1, 5, 3, 4]
    B_sample_4 = [2, 3, 4, 5]
    result4 = find_first_zero_difference_index(A_sample_4, B_sample_4)
    print(result4)
    A_sample_5 = [1, 2, 3]
    B_sample_5 = [4, 5, 6]
    result5 = find_first_zero_difference_index(A_sample_5, B_sample_5)
    print(result5)