def sort_by_descending(numbers):
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    sample_values = [29, 13, 8, 45, 6]
    sorted_values = sort_by_descending(sample_values)
    print(sorted_values)