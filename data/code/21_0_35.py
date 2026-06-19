def sort_by_descending(nums):
    return sorted(nums, reverse=True)

if __name__ == '__main__':
    sample_values = [34, 7, 23, 32, 5, 62]
    sorted_values = sort_by_descending(sample_values)
    print(sorted_values)