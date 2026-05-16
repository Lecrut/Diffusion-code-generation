def compare_lengths(list1, list2):
    all_lengths = list1 + list2
    if not all_lengths:
        return 0
    maximum = max(all_lengths)
    minimum = min(all_lengths)
    return maximum - minimum
if __name__ == '__main__':
    list_a = [10, 20, 30]
    list_b = [5, 15, 25]
    result = compare_lengths(list_a, list_b)
    print(result)