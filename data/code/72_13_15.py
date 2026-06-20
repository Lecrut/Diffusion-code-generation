def compare_elements_at_indices(list1, list2, indices):
    result = []
    for i in indices:
        if 0 <= i < len(list1) and 0 <= i < len(list2):
            result.append(list1[i] == list2[i])
        else:
            result.append(False)
    return result

if __name__ == '__main__':
    print(compare_elements_at_indices([1, 2, 3], [4, 5, 6], [0, 2]))
    print(compare_elements_at_indices(['a', 'b'], ['c', 'd', 'e'], [1, 2]))