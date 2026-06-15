import sys
def calculate_range(numbers):
    if not numbers:
        return 0
    minimum = min(numbers)
    maximum = max(numbers)
    return maximum - minimum
if __name__ == '__main__':
    sample_numbers = [10, 5, 22, 3, 18]
    result = calculate_range(sample_numbers)
    print(result)