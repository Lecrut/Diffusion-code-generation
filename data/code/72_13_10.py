def compare_elements_at_indices(list1, list2, indices):
    return [list1[i] == list2[i] if i < len(list1) and i < len(list2) else False for i in indices]

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 4, 6]
    indices = [0, 2, 4, 5]
    print(compare_elements_at_indices(list1, list2, indices))