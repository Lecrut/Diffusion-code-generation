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
    idx_valid = 2
    idx_invalid = 5
    result1 = compare_elements(list_a, list_b, idx_valid)
    print(f"Comparing lists with index {idx_valid}: Element from list_a is {result1[0]}, Element from list_b is {result1[1]}")
    result2 = compare_elements(list_a, list_b, idx_invalid)
    print(f"Comparing lists with index {idx_invalid}: Element from list_a is {result2[0]}, Element from list_b is {result2[1]}")