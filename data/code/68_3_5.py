def validate_lists(A, B):
    if len(A) != len(B):
        raise ValueError("Lists A and B must be of the same length.")

def compute_differences(A, B):
    return [a - b for a, b in zip(A, B)]

if __name__ == '__main__':
    A = [4, 8, 12]
    B = [2, 6, 10]
    validate_lists(A, B)
    differences = compute_differences(A, B)
    print(differences)