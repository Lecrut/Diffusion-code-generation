def determine_parity(number: int) -> None:
    """Check if a number is even or odd using the modulo operator."""
    remainder = number % 2
    
    # Determine parity based on the result of the modulus operation
    if remainder == 0:
        print(f"The integer {number} is an EVEN number.")
    else:
        print(f"The integer {number} is an ODD number.")

def main() -> None:
    """Main execution block with hard-coded sample values."""
    
    # Define a list of sample integers to test automatically
    samples = [0, 1, 23, -45]
    
    for num in samples:
        determine_parity(num)

if __name__ == '__main__':
    main()