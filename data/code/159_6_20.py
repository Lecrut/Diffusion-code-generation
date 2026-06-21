def is_valid_numbers(numbers):
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements must be integers")

def odd_numbers(numbers):
    is_valid_numbers(numbers)
    for number in numbers:
        if number % 2 != 0:
            yield number

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_gen = odd_numbers(sample_list)
    for _ in range(len(sample_list) // 2):
        print(next(odd_gen))