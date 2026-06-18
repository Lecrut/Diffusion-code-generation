import sys

def check_negative(num: float) -> bool:
    """Check if a given number is negative."""
    return num < 0

if __name__ == '__main__':
    # Sample values to test without user input
    sample_values = [-5.2, 10, -3]

    for value in sample_values:
        result = check_negative(value)
        print(f"Is {value} negative? {result}")