def sort_by_descending(numbers):
    descending_numbers = sorted(numbers, reverse=True)
    return descending_numbers

if __name__ == '__main__':
    initial_values = [10, 23, -5, 0, 17, 8]
    result = sort_by_descending(initial_values)
    print(result)