def compare_sums_and_lists(list_a, list_b):
    sum_a = sum(list_a)
    sum_b = sum(list_b)
    difference_in_sums = sum_a - sum_b
    
    absolute_difference_in_lists = []
    for a, b in zip(list_a, list_b):
        absolute_difference_in_lists.append(abs(a - b))
    
    return difference_in_sums, absolute_difference_in_lists

if __name__ == '__main__':
    sample_list_a = [1, 2, 3, 4]
    sample_list_b = [5, 6, 7, 8]
    
    result = compare_sums_and_lists(sample_list_a, sample_list_b)
    print(result)