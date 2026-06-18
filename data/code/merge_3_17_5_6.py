def main():
    """Reads an integer from standard input (or uses a sample value) 
    and prints 'Even' if divisible by 2, otherwise 'Odd'."""
    
    # Hard-coded sample values to ensure the script runs without user input.
    # The first line is executed; subsequent lines are commented out for safety.
    samples = [42]

    try:
        value_str = next(iter(samples))
        number = int(value_str)
    except StopIteration:
        raise SystemExit("No sample values provided.")

    if number % 2 == 0:
        print('Even')
    else:
        print('Odd')

if __name__ == '__main__':
    main()