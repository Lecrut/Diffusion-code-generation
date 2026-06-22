def sort_by_descending(numbers):
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    sample_numbers = [5, 3, 9, 1, 4]
    sorted_numbers = sort_by_descending(sample_numbers)
    print(sorted_numbers)