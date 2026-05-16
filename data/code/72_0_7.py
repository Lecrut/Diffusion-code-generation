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
    list_b = [11, 22, 33, 44]
    index_to_check = 2
    result1, result2 = compare_elements(list_a, list_b, index_to_check)
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    print(f"Index: {index_to_check}")
    print(f"Element from List A at index {index_to_check}: {result1}")
    print(f"Element from List B at index {index_to_check}: {result2}")
    index_out_of_bounds = 5
    result3, result4 = compare_elements(list_a, list_b, index_out_of_bounds)
    print(f"\nIndex: {index_out_of_bounds}")
    print(f"Element from List A at index {index_out_of_bounds}: {result3}")
    print(f"Element from List B at index {index_out_of_bounds}: {result4}")