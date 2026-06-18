def filter_even_numbers(numbers: list[int]) -> list[int]:
    """Returns a new list containing only the even numbers from the input list."""
    return [num for num in numbers if num % 2 == 0]

if __name__ == '__main__':
    sample_data = [1, 4, 7, 8, 9, 10]
    result = filter_even_numbers(sample_data)
    print(result)