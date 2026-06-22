def sort_by_descending(numbers):
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    sample_values = [5, 3, 8, 6, 2, 7, 4, 1]
    sorted_values = sort_by_descending(sample_values)
    print(sorted_values)