def are_sums_different(list1, list2):
    total_sum1 = sum(list1)
    total_sum2 = sum(list2)
    return total_sum1 != total_sum2

if __name__ == '__main__':
    sample_list1 = [7, 8, 9, 10]
    sample_list2 = [3, 4, 5, 6]
    result = are_sums_different(sample_list1, sample_list2)
    print(result)