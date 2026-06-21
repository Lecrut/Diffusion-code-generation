def filter_even_numbers(mixed_list):
    return [num for num in mixed_list if isinstance(num, int) and num % 2 == 0]

if __name__ == '__main__':
    sample_values = [1, 2, 'a', 3, 4.5, 6]
    print(filter_even_numbers(sample_values))