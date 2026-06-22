def find_unique_differences(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1 & set2
    diff1 = set1 - intersection
    diff2 = set2 - intersection
    return sorted(diff1), sorted(diff2)

if __name__ == '__main__':
    list_a = [1.0, 2.0, 3.0, 4.0, 5.0]
    list_b = [3.0, 4.0, 5.0, 6.0, 7.0]
    result_diff1, result_diff2 = find_unique_differences(list_a, list_b)
    print(f"Difference in List A: {result_diff1}")
    print(f"Difference in List B: {result_diff2}")