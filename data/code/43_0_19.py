def calculate_square_area(side_length):
    """
    Calculate the area of a square given its side length.
    
    Parameters:
        side_length (float or int): The length of one side of the square. Must be non-negative.
        
    Returns:
        float: The calculated area of the square.
        
    Raises:
        ValueError: If the side_length is negative.
    """
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    
    return side_length * side_length

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes only.
    # No user input, command-line arguments, or network access is used here.
    samples = [5.0, 10, -3]

    for s in samples:
        try:
            area = calculate_square_area(s)
            print(f"Side length {s} -> Area: {area}")
        except ValueError as e:
            print(e)