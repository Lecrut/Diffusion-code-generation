def is_even_number(num):
    return isinstance(num, int) and num % 2 == 0

def filter_even_numbers(mixed_list):
    if not all(isinstance(item, (int, float)) for item in mixed_list):
        raise ValueError("List contains non-numeric elements")
    return [item for item in mixed_list if is_even_number(item)]

if __name__ == '__main__':
    sample_values = [10, 'b', 3, 4, 5.5, 6]
    try:
        even_numbers = filter_even_numbers(sample_values)
        print(even_numbers)
    except ValueError as e:
        print(e)