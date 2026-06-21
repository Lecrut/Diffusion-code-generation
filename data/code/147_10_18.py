def timsort(arr):
    return sorted(arr)

if __name__ == '__main__':
    sample = [34, 7, 23, 32, 5, 62]
    print(timsort(sample))
    empty_list = []
    print(timsort(empty_list))
    duplicate_values = [1, 2, 2, 3, 3, 3]
    print(timsort(duplicate_values))