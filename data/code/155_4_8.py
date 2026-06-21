def validate_numbers(numbers):
    if not isinstance(numbers, list) or not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Input must be a list of numbers")

def sum_numbers(numbers):
    validate_numbers(numbers)
    return sum(numbers)

if __name__ == '__main__':
    sample1 = [4, 5, 6]
    sample2 = []
    print(sum_numbers(sample1))
    print(sum_numbers(sample2))