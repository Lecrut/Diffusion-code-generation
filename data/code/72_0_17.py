def compare_elements(list1, list2, index):
    try:
        element1 = list1[index]
    except IndexError:
        element1 = None
    try:
        element2 = list2[index]
    except IndexError:
        element2 = None
    return element1, element2

if __name__ == '__main__':
    sample_list_a = [10, 20, 30, 40, 50]
    sample_list_b = [11, 22, 33, 44, 55]
    index_to_compare = 3
    result = compare_elements(sample_list_a, sample_list_b, index_to_compare)
    print(f"List A: {sample_list_a}")
    print(f"List B: {sample_list_b}")
    print(f"Index: {index_to_compare}")
    print(f"Result: {result}")

    invalid_index = 10
    result_invalid = compare_elements(sample_list_a, sample_list_b, invalid_index)
    print(f"Comparing lists with index {invalid_index}: Element from list_a is {result_invalid[0]}, Element from list_b is {result_invalid[1]}")