def compare_elements_at_indices(list1, list2, indices):
    return [list1[idx] == list2[idx] if idx < len(list1) and idx < len(list2) else False for idx in indices]

if __name__ == '__main__':
    print(compare_elements_at_indices([1, 2, 3], [4, 5, 6], [0, 2]))
    print(compare_elements_at_indices(['a', 'b'], ['c', 'd', 'e'], [1, 2]))