def calculate_square_area(side_length):
    """
    Calculates the area of a square given its side length.
    
    Args:
        side_length (float | int): The length of one side of the square.
        
    Returns:
        float: The calculated area of the square.
    """
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or CLI arguments
    samples = [5, -3.0, 1e6]
    
    print("Sample Input-Output Results:")
    for value in samples:
        area = calculate_square_area(value)
        if isinstance(value, float):
            print(f"Input {value} -> Output {area}")
        else:
            print(f"Input {value} -> Output {int(area)}")