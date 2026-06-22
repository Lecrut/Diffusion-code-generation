def find_matching_indices(list1, list2):
    matching_indices = []
    for index, (value1, value2) in enumerate(zip(list1, list2)):
        if abs(value1 - value2) < 1e-09:
            matching_indices.append(index)
    return matching_indices
if __name__ == '__main__':
    sample_list1 = [1.0, 2.5, 3.0, 4.5]
    sample_list2 = [1.0, 2.6, 3.0, 4.5]
    print(find_matching_indices(sample_list1, sample_list2))