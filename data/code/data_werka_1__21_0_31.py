def sort_by_descending(numbers):
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    sample_values = [34, 1, 99, 23, 78]
    sorted_values = sort_by_descending(sample_values)
    print(sorted_values)