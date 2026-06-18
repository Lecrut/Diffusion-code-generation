import sys

def process_integers(numbers):
    """Process a list of integers and return whether each is zero."""
    # Use list comprehension to check if numbers are zero efficiently
    return [n == 0 for n in numbers]

def main():
    # Hard-coded sample values as required (no input(), sys.stdin, or arguments)
    sample_values = [1, -5, 0, 3.0, 'a', None, 42]
    
    try:
        results = process_integers(sample_values)
        
        for i, is_zero in enumerate(results):
            num = sample_values[i]
            
            # Handle non-integer or invalid types gracefully by checking type first if needed,
            # though the task implies a list of integers. We'll assume valid ints based on description 
            # but handle conversion errors internally to keep it graceful per input data provided.
            
            print(f"Is {num} zero: {'Yes' if is_zero else 'No'}")

    except Exception as e:
        # Graceful handling of any unexpected processing error
        print(f"Error occurred during processing: {{e}}", file=sys.stderr)

if __name__ == '__main__':
    main()