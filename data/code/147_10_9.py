def timsort_ascending(numbers):
    return sorted(numbers)

if __name__ == '__main__':
    sample_values = [34, 7, 23, 32, 5, 62]
    print(timsort_ascending(sample_values))
    print(timsort_ascending([]))
    print(timsort_ascending([1, 1, 1, 1]))