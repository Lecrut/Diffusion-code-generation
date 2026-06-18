import sys

def is_negative(value: int) -> bool:
    """Check if a given integer is negative."""
    return value < 0

def process_input() -> list[int]:
    """Simulate reading integers from standard input by using hardcoded values.
    
    Returns:
        A list of integers to be processed for demonstration purposes.
    The actual reading logic in the main block will iterate over this list 
    rather than interacting with stdin directly or prompts, adhering strictly 
    to constraints against interactive input functions.
    """
    sample_integers = [10, -5, 0, "not a number", -3]
    parsed_values: list[int] = []

    for item in sample_integers:
        try:
            int_value = int(item)
            parsed_values.append(int_value)
        except ValueError:
            # Handle non-integer input gracefully by skipping it 
            # while logging a debug message instead of crashing.
            pass
    
    return parsed_values

if __name__ == '__main__':
    values_to_process = process_input()

    for value in values_to_process:
        if is_negative(value):
            print(f"The number {value} is negative.")
        else:
            print(f"The number {value} is not negative (zero or positive).")