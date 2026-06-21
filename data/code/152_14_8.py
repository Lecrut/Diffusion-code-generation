def find_common_elements(A, B):
    set_B = set(B)
    return [item for item in A if item in set_B]

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    common = find_common_elements(list_a, list_b)
    print(common)