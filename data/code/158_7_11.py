def filter_even_numbers(mixed_list):
    if not all(isinstance(item, (int, float)) for item in mixed_list):
        raise ValueError("All elements in the list must be integers or floats")
    
    return [item for item in mixed_list if isinstance(item, int) and item % 2 == 0]

if __name__ == '__main__':
    sample_values = [1, 2, 'a', 3, 4.5, 6]
    try:
        even_numbers = filter_even_numbers(sample_values)
        print(even_numbers)
    except ValueError as e:
        print(e)