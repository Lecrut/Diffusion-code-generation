def compare_elements_at_indices(list1, list2, indices):
    return [list1[idx] == list2[idx] if 0 <= idx < len(list1) else False for idx in indices]

if __name__ == '__main__':
    print(compare_elements_at_indices([1, 2, 3], [1, 4, 3], [0, 1, 2]))
    print(compare_elements_at_indices(['a', 'b'], ['a', 'c'], [0, 2]))