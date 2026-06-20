def compare_elements_at_indices(list1, list2, indices):
    result = []
    for index in indices:
        if 0 <= index < len(list1) and 0 <= index < len(list2):
            result.append(list1[index] == list2[index])
        else:
            result.append(False)
    return result

if __name__ == '__main__':
    print(compare_elements_at_indices([1, 2, 3], [4, 5, 6], [0, 2]))
    print(compare_elements_at_indices(['a', 'b'], ['c', 'd', 'e'], [1, 2]))