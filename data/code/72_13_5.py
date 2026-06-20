def compare_elements_at_indices(list1, list2, indices):
    return [list1[i] == list2[i] if i < len(list1) and i < len(list2) else False for i in indices]

if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [1, 2, 5, 4]
    indices = [0, 2, 3]
    print(compare_elements_at_indices(list1, list2, indices))