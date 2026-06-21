def is_even(number):
    return number % 2 == 0

def filter_odd_numbers(numbers):
    return list(filter(is_even, numbers))

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = filter_odd_numbers(sample_numbers)
    print(even_numbers)