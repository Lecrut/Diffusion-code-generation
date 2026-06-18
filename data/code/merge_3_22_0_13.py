import sys

def is_odd_or_even(number):
    """Determine if a given integer is odd or even."""
    return number % 2 == 0

if __name__ == '__main__':
    # Sample values to test the logic without user input
    sample_values = [1, -3, 4, 10]

    for value in sample_values:
        if is_odd_or_even(value):
            status = "even"
        else:
            status = "odd"
        
        print(f"The number {value} is {status}.")