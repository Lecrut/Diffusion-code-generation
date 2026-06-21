def find_common_elements(A, B):
    if not isinstance(A, list) or not isinstance(B, list):
        raise ValueError("Both inputs must be lists")
    
    set_a = set(A)
    common_elements = [item for item in B if item in set_a]
    return common_elements

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    print(find_common_elements(sample_list1, sample_list2))