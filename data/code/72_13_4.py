def compare_elements_at_indices(list1, list2, indices):
    return [list1[i] == list2[i] if 0 <= i < len(list1) else False for i in indices]

if __name__ == '__main__':
    result = compare_elements_at_indices([1, 2, 3], [1, 4, 5], [0, 1, 2, 3])
    print(result)