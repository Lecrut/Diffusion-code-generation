def count_matching_positions(list1, list2):
    return sum(val1 == val2 for val1, val2 in zip(list1, list2))

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 2, 5, 5, 4, 1]
    sample_list2 = [1, 2, 2, 2, 5, 5, 4, 0]
    matching_count = count_matching_positions(sample_list1, sample_list2)
    print(matching_count)