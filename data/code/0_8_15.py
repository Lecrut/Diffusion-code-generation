def length_converter(length: float) -> None:
    """Converts a given length to miles and kilometers based on standard conversion factors."""
    
    # Conversion constants
    KILOMETER_PER_MILE = 1.60934
    
    # Perform conversions
    kilometers = length * KILOMETER_PER_MILE
    miles = length / KILOMETER_PER_MILE
    
    # Format output to two decimal places using f-string formatting
    print(f"Length: {length} units")
    print(f"Miles: {miles:.2f}")
    print(f"Kilometers: {kilometers:.2f}")

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without interactive input
    samples = [1, 5.5, 10]
    
    for length in samples:
        length_converter(length)