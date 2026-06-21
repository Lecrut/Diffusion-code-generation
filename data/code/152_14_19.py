def validate_input(A, B):
    if not all(isinstance(item, (int, str)) for item in A + B):
        raise ValueError("Both lists must contain only integers or strings.")

def find_common_elements(A, B):
    validate_input(A, B)
    return list(set(A) & set(B))

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5, 5]
    list_b = [4, 5, 6, 7, 8, 4]
    common = find_common_elements(list_a, list_b)
    print(common)