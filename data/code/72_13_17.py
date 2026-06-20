def compare_elements_at_indices(list1, list2, indices):
    return [list1[i] == list2[i] if i >= 0 and i < len(list1) and i < len(list2) else False for i in indices]

if __name__ == '__main__':
    result = compare_elements_at_indices([1, 2, 3], [4, 5, 6], [0, 2])
    print(result)