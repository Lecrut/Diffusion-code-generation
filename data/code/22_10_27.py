def extract_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    sample_values = [17, 42, 5, 24, 9, 33, 8]
    odd_numbers = extract_odd_numbers(sample_values)
    print(odd_numbers)