def sort_by_descending(arr):
    return sorted(arr, reverse=True)

if __name__ == '__main__':
    sample_values = [34, 12, 99, 87, 56, 23]
    sorted_values = sort_by_descending(sample_values)
    print(sorted_values)