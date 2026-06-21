MAX_FLOAT = float('inf')
MIN_FLOAT = -float('inf')

def calculate_range(numbers):
    if not numbers:
        return None
    minimum = min(numbers, default=MAX_FLOAT)
    maximum = max(numbers, default=MIN_FLOAT)
    return maximum - minimum

if __name__ == '__main__':
    sample_numbers = [10.5, 5.2, 22.8, 8.3, 15.7]
    result = calculate_range(sample_numbers)
    print(result)