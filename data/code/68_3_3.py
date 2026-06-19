def calculate_differences(A, B):
    if len(A) != len(B):
        raise ValueError("Lists A and B must be of the same length.")
    return [a - b for a, b in zip(A, B)]

if __name__ == '__main__':
    A = [7, 14, 21]
    B = [3, 6, 9]
    try:
        differences = calculate_differences(A, B)
        print(differences)
    except ValueError as e:
        print(e)