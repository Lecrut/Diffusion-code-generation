def compute_difference_sum(list1, list2):
    min_length = min(len(list1), len(list2))
    difference_sum = 0
    for index in range(min_length):
        difference = list1[index] - list2[index]
        difference_sum += difference
    return difference_sum
if __name__ == '__main__':
    sample_list1 = [9, 18, 27, 36, 45]
    sample_list2 = [1, 2, 3, 4]
    result = compute_difference_sum(sample_list1, sample_list2)
    print(result)