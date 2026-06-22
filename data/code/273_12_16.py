def filter_and_repeat_evens(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    return [item for item in evens for _ in range(2)]

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    repeated_evens = filter_and_repeat_evens(sample_numbers)
    print(repeated_evens)