def filter_even_numbers(mixed_list):
    return [item for item in mixed_list if isinstance(item, int) and item % 2 == 0]

if __name__ == '__main__':
    sample_values = [10, 'b', 3, 4, 5.5, 6]
    even_numbers = filter_even_numbers(sample_values)
    print(even_numbers)