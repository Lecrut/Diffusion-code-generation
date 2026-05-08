def find_common_elements(A, B):
    return list(set(A) & set(B))
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5, 6]
    list_b = [5, 6, 7, 8, 9, 1]
    common = find_common_elements(list_a, list_b)
    print(common)