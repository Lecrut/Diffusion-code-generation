def is_valid_number(num):
    return isinstance(num, int) and num % 2 == 0

def filter_even_numbers(mixed_list):
    return [item for item in mixed_list if is_valid_number(item)]

if __name__ == '__main__':
    sample_values = [1, 2, 'a', 3, 4.5, 6]
    print(filter_even_numbers(sample_values))