def count_matching_elements(arr1, arr2):
    count = 0
    min_length = min(len(arr1), len(arr2))
    for i in range(min_length):
        if arr1[i] == arr2[i]:
            count += 1
    return count

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [1, 2, 4, 4, 6]
    match_count = count_matching_elements(sample_list1, sample_list2)
    print(match_count)