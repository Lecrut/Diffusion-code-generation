def repeat_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0] * 2

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    repeated_evens = repeat_even_numbers(sample_numbers)
    print(repeated_evens)