def timsort_ascending(lst):
    return sorted(lst)

if __name__ == '__main__':
    sample_list = [34, 7, 23, 32, 5, 62]
    print(timsort_ascending(sample_list))
    empty_list = []
    print(timsort_ascending(empty_list))
    duplicate_values = [1, 2, 2, 3, 3, 3]
    print(timsort_ascending(duplicate_values))