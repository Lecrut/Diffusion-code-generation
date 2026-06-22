def filter_and_repeat_evens(numbers):
    if not all(isinstance(x, int) for x in numbers):
        raise ValueError("All elements must be integers.")
    
    evens = [x for x in numbers if x % 2 == 0]
    repeated_evens = [item for number in evens for item in (number, number)]
    return repeated_evens

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_and_repeat_evens(sample_numbers)
    print(result)