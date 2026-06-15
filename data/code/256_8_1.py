import sys
def calculate_range(numbers):
    if not numbers:
        return "No numbers provided."
    minimum = min(numbers)
    maximum = max(numbers)
    return f"The range is from {minimum} to {maximum}."
if __name__ == '__main__':
    sample_numbers = [15, 3, 88, 42, 9]
    result = calculate_range(sample_numbers)
    print(result)