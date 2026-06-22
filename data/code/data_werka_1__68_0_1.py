def sum_of_differences(list1, list2):
    min_length = min(len(list1), len(list2))
    truncated_list1 = list1[:min_length]
    truncated_list2 = list2[:min_length]
    total_difference = sum((a - b for a, b in zip(truncated_list1, truncated_list2)))
    return total_difference
if __name__ == '__main__':
    sample_list1 = [5, 10, 15, 20]
    sample_list2 = [3, 8, 12, 18]
    result = sum_of_differences(sample_list1, sample_list2)
    print(result)