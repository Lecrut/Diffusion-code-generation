def filter_even_numbers(number_list):
    if not all(isinstance(x, int) for x in number_list):
        raise ValueError("All elements in the list must be integers.")
    return [num for num in number_list if num % 2 == 0]

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    print(filter_even_numbers(sample_numbers))