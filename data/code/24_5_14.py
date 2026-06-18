import sys

def check_sign(number: int) -> str:
    """Determine if a number is negative."""
    return "negative" if number < 0 else "non-negative"

if __name__ == '__main__':
    # Hard-coded sample values to avoid user input, arguments, or network access.
    samples = [10, -5, 0, -3, 2]
    
    for item in samples:
        try:
            num = int(item)
            print(f"{num} is {check_sign(num)}")
        except ValueError as e:
            # This block handles non-integer input (though the sample list contains only ints).
            if isinstance(e, TypeError):
                print("Error: Input must be an integer.")
            else:
                print(f"Input error occurred for value {item}.", file=sys.stderr)