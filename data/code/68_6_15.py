def max_difference(A, B):
    min_A = min(A)
    max_B = max(B)
    return abs(max_B - min_A)

if __name__ == '__main__':
    A = [3, 10, 6]
    B = [1, 4, 8]
    print(max_difference(A, B))