def sort_by_descending(numbers):
    if not numbers:
        return []
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    sample_values = [7, 2, 9, 4, 5]
    sorted_values = sort_by_descending(sample_values)
    print(sorted_values)