def max_difference(A, B):
    if not A or not B:
        raise ValueError("Both lists must contain at least one element.")
    
    min_A = min(A)
    max_A = max(A)
    min_B = min(B)
    max_B = max(B)
    
    return max(max_A - min_B, max_B - min_A)

if __name__ == '__main__':
    A = [3, 10, 6]
    B = [1, 4, 8]
    print(max_difference(A, B))