def sort_by_descending(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers

if __name__ == '__main__':
    initial_values = [7, 2, 5, 3, 8, -1, 4]
    result = sort_by_descending(initial_values)
    print(result)