SHARED_ELEMENTS = set()

def find_common_elements(A, B):
    A_set = set(A)
    SHARED_ELEMENTS.update(item for item in B if item in A_set)

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5, 5]
    list_b = [4, 5, 6, 7, 8, 4]
    find_common_elements(list_a, list_b)
    print(SHARED_ELEMENTS)