def compute_differences(A, B):
    return [a - b for a, b in zip(A, B)]

if __name__ == '__main__':
    A = [9, 18, 27]
    B = [4, 8, 12]
    differences = compute_differences(A, B)
    print(differences)