def extract_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

if __name__ == '__main__':
    SAMPLE_VALUES = [15, 22, 37, 40, 53, 68, 75, 82, 91, 100]
    even_numbers = extract_even_numbers(SAMPLE_VALUES)
    print(even_numbers)