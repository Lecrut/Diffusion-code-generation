def filter_numbers(numbers, divisible_by=2, is_even=True):
    return [num for num in numbers if (num % divisible_by == 0) == is_even]
if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered_numbers = filter_numbers(sample_numbers, divisible_by=2, is_even=True)
    print(filtered_numbers)