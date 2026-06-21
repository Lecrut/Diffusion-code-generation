MAX_VALUE = float('inf')
MIN_VALUE = float('-inf')

def calculate_range(numbers):
    if not numbers:
        return None
    minimum = min(numbers, default=MAX_VALUE)
    maximum = max(numbers, default=MIN_VALUE)
    return maximum - minimum

if __name__ == '__main__':
    sample_numbers = [10, 5, 22, 8, 15]
    result = calculate_range(sample_numbers)
    print(result)