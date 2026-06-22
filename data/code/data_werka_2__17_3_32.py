def get_even_numbers(numbers):
    EVEN_THRESHOLD = 2
    return [num for num in numbers if num % EVEN_THRESHOLD == 0]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = get_even_numbers(sample_values)
    print(even_numbers)