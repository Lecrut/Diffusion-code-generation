def compare_elements(list1, list2, index):
    try:
        return list1[index], list2[index]
    except IndexError:
        return None, None

if __name__ == '__main__':
    list_a = [10, 20, 30, 40]
    list_b = [5, 15, 25, 35]
    index_to_check = 2
    result = compare_elements(list_a, list_b, index_to_check)
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    print(f"Index: {index_to_check}")
    print(f"Result: {result}")

    invalid_index = 5
    result_invalid = compare_elements(list_a, list_b, invalid_index)
    print(f"Comparing lists with index {invalid_index}: Result is {result_invalid}")