def validate_input(numbers):
    if not isinstance(numbers, list) or not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Input must be a list of numbers")

def calculate_sum(numbers):
    validate_input(numbers)
    return sum(numbers)

if __name__ == '__main__':
    sample_list = [1, 5, 10, 2]
    result = calculate_sum(sample_list)
    print(result)