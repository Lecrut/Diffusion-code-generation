def get_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    sample_values = [15, 24, 37, 48, 59, 60, 71, 82, 93, 104]
    odd_numbers = get_odd_numbers(sample_values)
    print(odd_numbers)