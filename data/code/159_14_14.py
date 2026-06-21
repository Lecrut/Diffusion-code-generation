def filter_odd_numbers(numbers: list[int]) -> list[int]:
    if not isinstance(numbers, list) or not all(isinstance(num, int) for num in numbers):
        raise ValueError("Input must be a list of integers")
    
    return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(filter_odd_numbers(sample_values))