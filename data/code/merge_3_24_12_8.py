# Script to filter negative integers from a list of numbers.
# This module demonstrates filtering using a generator expression within print().

def is_negative(num):
    """Returns True if the number is strictly less than zero, False otherwise."""
    return num < 0

if __name__ == '__main__':
    # Hard-coded sample values representing integers to be processed.
    numbers = [10, -5, 3, -20, 7, -8]

    # Using a generator expression inside print() to filter negative numbers efficiently.
    # This approach avoids creating an intermediate list in memory and is generally preferred for readability when processing single pass data.
    filtered_numbers = (n for n in numbers if is_negative(n))

    # Printing each negative number found, separated by spaces.
    print(" ".join(str(num) for num in filtered_numbers))