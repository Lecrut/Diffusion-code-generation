def print_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    for number in even_numbers:
        print(number)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print_even_numbers(sample_values)