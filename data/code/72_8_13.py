def validate_lists(list1, list2):
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise ValueError("Both arguments must be lists.")
    if len(list1) != len(list2):
        raise ValueError("Lists must be of the same length.")

def compare_elements(list1, list2, index):
    validate_lists(list1, list2)
    if not (0 <= index < len(list1)):
        raise IndexError("Index out of range.")
    return list1[index] == list2[index]

if __name__ == '__main__':
    list_a = [10, 20, 30]
    list_b = [10, 20, 30]
    idx = 1
    result = compare_elements(list_a, list_b, idx)
    print(result)

    list_c = [5, 15, 25]
    list_d = [5, 15, 25]
    idx = 2
    result = compare_elements(list_c, list_d, idx)
    print(result)

    list_e = [100, 200]
    list_f = [100, 200]
    idx = 0
    result = compare_elements(list_e, list_f, idx)
    print(result)