import sys

def main():
    """Reads a list of integers from standard input (simulated via hard-coded data)
    and prints negative numbers using a generator expression."""
    
    # Hard-coded sample values as per requirements to avoid interactive prompts or file I/O.
    # This simulates the expected input format: one integer per line.
    raw_input_data = [10, -5, 3, -20, 7, -1, 4]

    # Use a generator expression with list() conversion to collect negative numbers efficiently.
    # Logic: Iterate through each number; if it is less than zero, include it in the result set.
    filtered_numbers = [num for num in raw_input_data if num < 0]

    # Print each of the resulting negative integers on a new line.
    print(f"Negative numbers found: {filtered_numbers}")

if __name__ == '__main__':
    main()