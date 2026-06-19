def compute_differences(A, B):
    if len(A) != len(B):
        raise ValueError("Lists A and B must be of the same length.")
    return [a - b for a, b in zip(A, B)]

if __name__ == '__main__':
    try:
        A = [10, 20, 30]
        B = [5, 15, 25]
        differences = compute_differences(A, B)
        print(differences)
    except ValueError as e:
        print(e)