def timsort(arr):
    return sorted(arr)

if __name__ == '__main__':
    sample_values = [34, 7, 23, 32, 5, 62]
    print(timsort(sample_values))
    empty_list = []
    print(timsort(empty_list))
    duplicate_values = [1, 3, 2, 1, 3, 2]
    print(timsort(duplicate_values))