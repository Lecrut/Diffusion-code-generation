def compare_elements(list1, list2, index):
    try:
        element1 = list1[index]
        element2 = list2[index]
        return element1, element2
    except IndexError:
        return None, None
if __name__ == '__main__':
    list_a = [10, 20, 30, 40]
    list_b = [11, 22, 33, 44]
    index_to_check = 2
    result = compare_elements(list_a, list_b, index_to_check)
    print(f"Comparing lists: {list_a} and {list_b} at index {index_to_check}")
    print(f"Result: {result}")
    list_c = [5, 6]
    list_d = [7, 8]
    index_out_of_bounds = 5
    result_error = compare_elements(list_c, list_d, index_out_of_bounds)
    print(f"\nComparing lists: {list_c} and {list_d} at index {index_out_of_bounds}")
    print(f"Result: {result_error}")