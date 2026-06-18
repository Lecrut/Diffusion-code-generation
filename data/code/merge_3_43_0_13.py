def calculate_square_area(side_length):
    """
    Calculate the area of a square given its side length.
    
    The formula used is: Area = side * side
    
    Args:
        side_length (float or int): The length of one side of the square.
        
    Returns:
        float: The calculated area of the square.
        
    Raises:
        ValueError: If the side length is negative.
    """
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    
    return side_length * side_length

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [5.0, 10, -3]

    print("Testing Square Area Calculator")
    print("-" * 20)

    for side in test_cases:
        try:
            area = calculate_square_area(side)
            print(f"Side length: {side}")
            print(f"Calculated Area: {area}\n")
        except ValueError as e:
            print(f"Error for input {side}: {e}\n")

    # Demonstration with a final clean example
    side_length = 7.5
    area_result = calculate_square_area(side_length)
    
    print("-" * 20)
    print(f"Final Example: Side length of {side_length}")
    print(f"The Area is {area_result} square units.")