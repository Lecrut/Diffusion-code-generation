def validate_lists(A, B):
    if len(A) != len(B):
        raise ValueError("Lists A and B must be of the same length.")

def compute_differences(A, B):
    return [a - b for a, b in zip(A, B)]

if __name__ == '__main__':
    A = [10, 20, 30, 40]
    B = [5, 15, 25, 35]
    try:
        validate_lists(A, B)
        differences = compute_differences(A, B)
        print(differences)
    except ValueError as e:
        print(e)