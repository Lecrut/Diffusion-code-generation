def calculate_square_area(side_length):
    """
    Calculate the area of a square given its side length.
    
    Args:
        side_length (float or int): The length of one side of the square. Must be non-negative.
        
    Returns:
        float: The calculated area of the square.
        
    Raises:
        ValueError: If the side_length is negative.
    """
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes without user input.
    test_cases = [5, 10.5, 0]
    
    print(f"Calculating area for a square with side length: {test_cases[0]}")
    result_1 = calculate_square_area(test_cases[0])
    print(f"The calculated area is: {result_1}")
    
    print(f"\nCalculating area for a square with side length: {test_cases[1]}")
    result_2 = calculate_square_area(test_cases[1])
    print(f"The calculated area is: {result_2}")
    
    print(f"\nCalculating area for a square with side length: {test_cases[2]}")
    result_3 = calculate_square_area(test_cases[2])
    print(f"The calculated area is: {result_3}")