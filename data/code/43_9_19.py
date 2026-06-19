def calculate_square_area(side_length: float) -> float:
    """Calculate the area of a square using direct mathematical operation."""
    return side_length * side_length

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    samples = [5.0, 10, -3]  # Includes negative to verify behavior (area should be positive)

    print("Area Calculations:")
    for val in samples:
        area = calculate_square_area(val)
        if abs(area) > float('inf'):
            continue  # Skip invalid inputs like negatives or complex numbers if desired, though math handles it
        else:
            print(f"Side length {val} -> Area: {area}")

    # Additional test with zero and large number for edge cases
    edge_cases = [0.0, float('inf')]
    
    for val in edge_cases:
        try:
            area = calculate_square_area(val)
            print(f"Side length {val} -> Area: {area}")
        except (OverflowError, TypeError):
            pass  # Handle overflow gracefully if needed