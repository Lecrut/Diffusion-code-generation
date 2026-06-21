def sort_by_descending(numbers):
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    sample_values = [7, 1, 5, 3, 9, 2]
    sorted_values = sort_by_descending(sample_values)
    print(sorted_values)