def filter_even_numbers(mixed_list):
    return [item for item in mixed_list if isinstance(item, int) and item % 2 == 0]

if __name__ == '__main__':
    sample_values = [15, 'c', 8, 9, 10.0, 12]
    even_numbers = filter_even_numbers(sample_values)
    print(even_numbers)