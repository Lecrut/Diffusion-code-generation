def validate_input(list1, list2):
    if not all(isinstance(x, int) for x in list1 + list2):
        raise ValueError("Both lists must contain only integers.")
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise TypeError("Both inputs must be lists.")

def intersect_sorted_lists(list1, list2):
    validate_input(list1, list2)
    i, j = 0, 0
    result = []
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            result.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return result

if __name__ == '__main__':
    sample_list1 = [1, 3, 5, 7, 9]
    sample_list2 = [0, 2, 4, 6, 8, 9]
    print(intersect_sorted_lists(sample_list1, sample_list2))