def sum_numbers(numbers):
    if not isinstance(numbers, list) or not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Input must be a list of numbers")
    return sum(numbers)

if __name__ == '__main__':
    sample1 = [7, 8, 9]
    sample2 = []
    print(sum_numbers(sample1))
    print(sum_numbers(sample2))