def filter_even_numbers(numbers_list):
    even_numbers = [num for num in numbers_list if num % 2 == 0]
    return even_numbers

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered_evens = filter_even_numbers(sample_numbers)
    print(filtered_evens)