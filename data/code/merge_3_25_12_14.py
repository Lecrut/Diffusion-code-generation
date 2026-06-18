import sys

def process_integers(numbers):
    """
    Takes a list of integers and returns a boolean indicating if each is zero.
    
    Args:
        numbers (list[int]): List of integers to check.
        
    Returns:
        list[bool]: A list where the i-th element corresponds to whether 
                   numbers[i] == 0.
    """
    return [num != 0 for num in numbers]

def main():
    # Hard-coded sample values as per requirements (no user input, args, or network)
    sample_data = [-5, 0, 3, -12, 7, 0, 42]

    try:
        result = process_integers(sample_data)
        
        # Print the results separated by space for clarity
        print(" ".join(map(str, result)))
            
    except Exception as e:
        # Graceful error handling without printing stack traces to stderr in a way that breaks flow
        print(f"Error processing data: {e}", file=sys.stderr)

if __name__ == '__main__':
    main()