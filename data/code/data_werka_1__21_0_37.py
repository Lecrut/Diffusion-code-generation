def sort_by_descending(arr):
    return sorted(arr, reverse=True)

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_values = sort_by_descending(sample_values)
    print(sorted_values)