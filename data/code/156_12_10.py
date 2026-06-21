def validate_input(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("Input must be a list of numbers")

def calculate_average(numbers):
    validate_input(numbers)
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    avg = calculate_average(sample_numbers)
    print(avg)