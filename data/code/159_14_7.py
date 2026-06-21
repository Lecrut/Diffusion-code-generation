def is_odd(number: int) -> bool:
    return number % 2 != 0

def filter_odd_numbers(numbers: list[int]) -> list[int]:
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements must be integers")
    
    odd_numbers = [num for num in numbers if is_odd(num)]
    return odd_numbers

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(filter_odd_numbers(sample_values))