import sys
def calculate_range(numbers):
    if not numbers:
        return None
    minimum = min(numbers)
    maximum = max(numbers)
    return maximum - minimum
if __name__ == '__main__':
    sample_input = "10 5 22 8 15"
    try:
        numbers = list(map(int, sample_input.split()))
        if not numbers:
            print("No numbers provided.")
        else:
            range_val = calculate_range(numbers)
            print(range_val)
    except ValueError:
        print("Error: Invalid input. Please ensure all inputs are integers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")