import sys
def calculate_range(numbers):
    if not numbers:
        return 0
    minimum = min(numbers)
    maximum = max(numbers)
    return maximum - minimum
if __name__ == '__main__':
    sample_numbers = [10, 5, 22, 8, 15]
    try:
        input_sequence = sample_numbers
        result = calculate_range(input_sequence)
        print(result)
    except Exception as e:
        print("An error occurred during calculation:", e)