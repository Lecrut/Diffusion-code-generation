def timsort_ascending(numbers):
    return sorted(numbers)

if __name__ == '__main__':
    sample_values = [34, 7, 23, 32, 5, 62]
    print(timsort_ascending(sample_values))
    empty_list = []
    print(timsort_ascending(empty_list))
    duplicate_values = [10, 20, 10, 30, 40, 20]
    print(timsort_ascending(duplicate_values))