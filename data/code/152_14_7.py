def is_valid_list(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    return True

def find_common_elements(A, B):
    is_valid_list(A)
    is_valid_list(B)
    return list(set(A) & set(B))

if __name__ == '__main__':
    sample_list_a = [1, 2, 3, 4, 5, 5]
    sample_list_b = [4, 5, 6, 7, 8, 4]
    common_elements = find_common_elements(sample_list_a, sample_list_b)
    print(common_elements)