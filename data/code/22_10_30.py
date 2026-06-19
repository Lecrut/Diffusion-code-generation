def is_odd(number):
    return number % 2 != 0

def filter_odds(numbers):
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list")
    for num in numbers:
        if not isinstance(num, int):
            raise ValueError("All elements in the list must be integers")
    return [num for num in numbers if is_odd(num)]

if __name__ == '__main__':
    sample_numbers = [10, 23, 45, 68, 77, 90]
    odd_numbers = filter_odds(sample_numbers)
    print(odd_numbers)