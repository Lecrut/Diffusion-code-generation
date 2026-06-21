def filter_even_numbers(mixed_list):
    even_numbers = []
    for item in mixed_list:
        if isinstance(item, int) and item % 2 == 0:
            even_numbers.append(item)
    return even_numbers

if __name__ == '__main__':
    sample_values = [15, 'b', 30, 45, 60]
    filtered_evens = filter_even_numbers(sample_values)
    print(filtered_evens)