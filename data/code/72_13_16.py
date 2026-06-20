def compare_elements_at_indices(list1, list2, indices):
    result = []
    for i in indices:
        try:
            if list1[i] == list2[i]:
                result.append(True)
            else:
                result.append(False)
        except IndexError:
            result.append(False)
    return result

if __name__ == '__main__':
    print(compare_elements_at_indices([1, 2, 3], [4, 5, 6], [0, 2]))
    print(compare_elements_at_indices(['a', 'b'], ['c', 'd', 'e'], [1, 2]))