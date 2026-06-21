def is_even(number):
    return number % 2 == 0

def filter_even_numbers(numbers_list):
    return [num for num in numbers_list if is_even(num)]

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = filter_even_numbers(sample_numbers)
    print(even_numbers)