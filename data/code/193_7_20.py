def validate_numbers(numbers):
    if not isinstance(numbers, list) or not all(isinstance(n, (int, float)) for n in numbers):
        raise ValueError("Input must be a list of numbers")

def calculate_sum(numbers):
    validate_numbers(numbers)
    return sum(numbers)

if __name__ == '__main__':
    data = [10, 25, 30, 45, 50]
    result = calculate_sum(data)
    print(result)