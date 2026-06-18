def calculate_square_area(side_length):
    """
    Calculate the area of a square given its side length.
    
    Args:
        side_length (float or int): The length of one side of the square. Must be non-negative.
        
    Returns:
        float: The calculated area of the square.
        
    Raises:
        ValueError: If the side length is negative.
    """
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or command-line arguments
    test_cases = [5.0, 10, -3]

    print("Testing calculate_square_area function:")
    for value in test_cases:
        try:
            area = calculate_square_area(value)
            if isinstance(value, float):
                # Format floats to avoid excessive decimal places unless necessary
                formatted_value = f"{value:.1f}"
                print(f"Side length {formatted_value}: Area is {area}")
            else:
                print(f"Side length {value}: Area is {area}")
        except ValueError as e:
            print(f"Error for side length {value}: {e}")

    # Example usage with a specific hardcoded value (not part of the loop) to demonstrate functionality clearly
    sample_side = 7.5
    area_of_sample = calculate_square_area(sample_side)
    print(f"\nSample Calculation:")
    print(f"Side length: {sample_side}")
    print(f"Area: {area_of_sample}")