def compare_elements_at_indices(list1, list2, indices):
    result = []
    for index in indices:
        if 0 <= index < len(list1) and 0 <= index < len(list2):
            result.append(list1[index] == list2[index])
        else:
            result.append(False)
    return result

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40]
    sample_list2 = [10, 25, 30, 45]
    sample_indices = [0, 2, 3, 4]
    print(compare_elements_at_indices(sample_list1, sample_list2, sample_indices))