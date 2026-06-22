def sort_by_descending(numbers):
    sorted_numbers = numbers.copy()
    sorted_numbers.sort(reverse=True)
    return sorted_numbers

if __name__ == '__main__':
    sample_values = [7, 2, 5, 3, 9, 1]
    result = sort_by_descending(sample_values)
    print(result)