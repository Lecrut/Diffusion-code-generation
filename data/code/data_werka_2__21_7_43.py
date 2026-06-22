def sort_by_descending(numbers):
    return sorted(numbers, reverse=True)

if __name__ == '__main__':
    example_values = [7, 2, 5, 3, 8, 6]
    descending_order = sort_by_descending(example_values)
    print(descending_order)