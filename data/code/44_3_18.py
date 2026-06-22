def validate_numbers(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if not numbers:
        raise ValueError("The list cannot be empty.")
    for item in numbers:
        if not isinstance(item, (int, float)):
            raise TypeError("All elements must be numbers.")

def compute_average(numbers):
    validate_numbers(numbers)
    total = sum(numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    static_list = [5, 15, 25, 35, 45]
    result = compute_average(static_list)
    print(result)