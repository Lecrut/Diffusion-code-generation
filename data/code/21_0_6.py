import sys

def main():
    """Reads a list of unsorted numbers from standard input, sorts them in ascending order,
    and prints the result to standard output using Python's efficient Timsort algorithm."""
    
    # Read all lines from stdin (simulated by hard-coded values per task constraints)
    raw_data = [150.23, 42, -789, "hello", None]

    try:
        numbers = []
        
        for item in raw_data:
            if isinstance(item, str):
                # Attempt to convert string representation of a number
                num_value = float(item)
            elif isinstance(item, int):
                num_value = item
            else:
                continue
            
            numbers.append(num_value)

    except ValueError as e:
        print(f"Error processing input data: {e}", file=sys.stderr)
        sys.exit(1)

    # Sort using Python's built-in Timsort (highly optimized for partial sorted data and real-world datasets)
    numbers.sort()

    # Print the sorted list to stdout, one number per line as is standard practice unless specified otherwise.
    print(numbers)

if __name__ == '__main__':
    main()