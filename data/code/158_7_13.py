def is_even(number):
    return isinstance(number, int) and number % 2 == 0

def filter_even_numbers(mixed_list):
    return [item for item in mixed_list if is_even(item)]

if __name__ == '__main__':
    sample_values = [1, 2, 'a', 3, 4.5, 6]
    even_numbers = filter_even_numbers(sample_values)
    print(even_numbers)