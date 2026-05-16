def find_first_zero_difference_index(A, B):
    n = min(len(A), len(B))
    for i in range(n - 1):
        if A[i] == B[i + 1]:
            return i
    return -1
if __name__ == '__main__':
    A1 = [1, 2, 3, 4, 5]
    B1 = [2, 3, 5, 6, 7]
    print(find_first_zero_difference_index(A1, B1))
    A2 = [10, 20, 30, 40]
    B2 = [10, 20, 30, 50]
    print(find_first_zero_difference_index(A2, B2))
    A3 = [1, 1, 3, 4]
    B3 = [1, 2, 4, 5]
    print(find_first_zero_difference_index(A3, B3))
    A4 = [5, 5, 1, 2]
    B4 = [5, 6, 3, 4]
    print(find_first_zero_difference_index(A4, B4))
    A5 = [1, 2, 3]
    B5 = [4, 5, 6]
    print(find_first_zero_difference_index(A5, B5))