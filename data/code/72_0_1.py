def compare_elements(list1, list2, index):
    try:
        element1 = list1[index]
    except IndexError:
        element1 = "Index out of bounds for list1"
    try:
        element2 = list2[index]
    except IndexError:
        element2 = "Index out of bounds for list2"
    return element1, element2
if __name__ == '__main__':
    list_a = [10, 20, 30, 40]
    list_b = [5, 15, 25, 35]
    index_to_check = 2
    result = compare_elements(list_a, list_b, index_to_check)
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    print(f"Index: {index_to_check}")
    print(f"Elements at index {index_to_check}: {result}")
    list_c = [1, 2]
    list_d = [3, 4, 5]
    index_out_of_bounds = 5
    result_error = compare_elements(list_c, list_d, index_out_of_bounds)
    print(f"\nList C: {list_c}")
    print(f"List D: {list_d}")
    print(f"Index: {index_out_of_bounds}")
    print(f"Elements at index {index_out_of_bounds}: {result_error}")