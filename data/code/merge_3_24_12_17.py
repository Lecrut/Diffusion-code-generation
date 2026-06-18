def main():
    """
    Reads a list of integers from standard input (or uses hard-coded values if stdin is empty/unused)
    and prints negative numbers using a generator expression.
    
    Since the requirement forbids interactive prompts, sys.stdin usage for user interaction, 
    or argparse required arguments, this script defaults to processing the provided sample data directly.
    """
    # Hard-coded sample list of integers as per requirements (no external files or network access)
    numbers = [10, -5, 3, -20, 7, -8, 0]

    # Use a generator expression to filter negative numbers efficiently
    # Generator expressions are memory-efficient for large datasets compared to list comprehensions
    negatives = (num for num in numbers if num < 0)

    # Print each filtered number on a new line
    print("\n".join(str(num) for num in negatives))

if __name__ == '__main__':
    main()