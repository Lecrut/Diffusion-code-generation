def combine_lists(list1, list2):
    return [item for sublist in (list1, list2) for item in sublist]

if __name__ == '__main__':
    sample_list1 = [7, 8, 9]
    sample_list2 = ['x', 'y']
    combined_result = combine_lists(sample_list1, sample_list2)
    print(combined_result)