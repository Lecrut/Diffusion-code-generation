def compare_elements_at_index(list1, list2, index):
    if index < 0 or index >= len(list1) or index >= len(list2):
        raise ValueError("Index out of range for one or both lists")
    return list1[index] <= list2[index]

if __name__ == '__main__':
    list_a = [10, 20, 30]
    list_b = [15, 10, 30]
    idx = 0
    result = compare_elements_at_index(list_a, list_b, idx)
    print(result)