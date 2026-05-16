def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_even_numbers(sample_list)
    print(result)