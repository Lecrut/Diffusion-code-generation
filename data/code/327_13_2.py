import sys
def calculate_running_total(numbers):
    running_total = 0
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError(f"Invalid input: '{num}' is not a number.")
        running_total += num
    return running_total
if __name__ == '__main__':
    sample_input = [10, 5.5, -2, 8]
    try:
        result = calculate_running_total(sample_input)
        print(f"The running total sum is: {result}")
    except TypeError as e:
        print(f"Error processing input: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)