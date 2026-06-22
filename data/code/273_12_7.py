def repeat_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0] * 2

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6]
    print(repeat_even_numbers(sample_values))