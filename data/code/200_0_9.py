def filter_even_numbers(number_list):
    if not isinstance(number_list, list) or not all((isinstance(i, int) for i in number_list)):
        raise ValueError('Input must be a list of integers.')
    return [n for n in number_list if n % 2 == 0]
if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    even_numbers = filter_even_numbers(sample_numbers)
    print(even_numbers)