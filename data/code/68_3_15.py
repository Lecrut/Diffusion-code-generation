def validate_lists(A, B):
    if len(A) != len(B):
        raise ValueError("Lists A and B must be of the same length.")

def calculate_differences(A, B):
    return [a - b for a, b in zip(A, B)]

if __name__ == '__main__':
    A = [100, 200, 300]
    B = [50, 100, 150]
    try:
        validate_lists(A, B)
        differences = calculate_differences(A, B)
        print(differences)
    except ValueError as e:
        print(e)