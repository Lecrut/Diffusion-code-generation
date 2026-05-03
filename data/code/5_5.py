def compare_lengths(list1, list2):
    if not list1 and not list2:
        return 0
    all_lengths = list1 + list2
    if not all_lengths:
        return 0
    maximum = max(all_lengths)
    minimum = min(all_lengths)
    range_difference = maximum - minimum
    return range_difference
if __name__ == '__main__':
    list_a = [10, 20, 30]
    list_b = [5, 15, 25]
    result = compare_lengths(list_a, list_b)
    print(result)