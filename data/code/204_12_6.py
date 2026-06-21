def validate_input(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, int) for x in numbers):
        raise ValueError("Input must be a list of integers")

def find_middle_value(numbers):
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        middle1 = numbers[n // 2 - 1]
        middle2 = numbers[n // 2]
        return (middle1 + middle2) / 2

def calculate_median(numbers):
    validate_input(numbers)
    sorted_numbers = sorted(numbers)
    return find_middle_value(sorted_numbers)

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("The median value is:", calculate_median(sample_values))