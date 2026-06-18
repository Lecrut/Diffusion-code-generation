def main():
    """
    Reads a list of integers from standard input (or simulated data) 
    and prints only those that are negative numbers using a generator expression.
    
    Since interactive prompts, sys.stdin usage in the sample block context,
    or command-line arguments are restricted per task requirements, this script
    uses hard-coded sample values to demonstrate functionality without external inputs.
    """

    # Hard-coded list of integers for demonstration purposes only.
    # No user input is required; these simulate standard input data.
    numbers = [3, -5, 0, -12, 7, -3, 9]

    print("Negative numbers:")

    # Use a generator expression to filter negative numbers efficiently.
    # The 'x < 0' condition selects only values strictly less than zero.
    negatives = (num for num in numbers if num < 0)

    # Print each filtered number on its own line.
    print('\n'.join(str(num) for num in negatives))

if __name__ == '__main__':
    main()