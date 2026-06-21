def timsort(lst):
    return sorted(lst)

if __name__ == '__main__':
    sample_list = [34, 7, 23, 32, 5, 62]
    print(timsort(sample_list))
    empty_list = []
    print(timsort(empty_list))
    duplicate_values = [1, 2, 2, 3, 4, 4, 5]
    print(timsort(duplicate_values))