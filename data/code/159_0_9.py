def filter_odd_numbers(numbers):
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements must be integers")
    return list(filter(lambda x: x % 2 != 0, numbers))

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_numbers = filter_odd_numbers(sample_numbers)
    print(odd_numbers)