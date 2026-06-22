def max_difference(A, B):
    min_A = min(A)
    max_A = max(A)
    min_B = min(B)
    max_B = max(B)
    
    return max(max_A - min_B, max_B - min_A)

if __name__ == '__main__':
    A = [1, 3, 5]
    B = [2, 4, 6]
    print(max_difference(A, B))