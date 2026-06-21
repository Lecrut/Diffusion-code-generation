def sort_by_descending(numbers):
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    sample_values = [15, 22, 3, 8, 9, 10]
    sorted_values = sort_by_descending(sample_values)
    print(sorted_values)