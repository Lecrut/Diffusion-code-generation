def timsort(arr):
    return sorted(arr)

if __name__ == '__main__':
    sample_list = [34, 7, 23, 32, 5, 62]
    print(timsort(sample_list))
    empty_list = []
    print(timsort(empty_list))
    duplicate_values = [1, 1, 1, 2, 2, 3, 3, 3]
    print(timsort(duplicate_values))