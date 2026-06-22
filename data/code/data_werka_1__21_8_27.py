def sort_by_descending(numbers):
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    sample_numbers = [34, 7, 23, 32, 5, 62]
    sorted_numbers = sort_by_descending(sample_numbers)
    print(sorted_numbers)