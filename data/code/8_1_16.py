def calculate_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle given its length and width.
    
    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
        
    Returns:
        float: The calculated area as length multiplied by width.
    """
    return length * width

if __name__ == '__main__':
    # Sample values for testing without user input or external dependencies
    sample_length = 5.0
    sample_width = 10.2
    
    result_area = calculate_area(sample_length, sample_width)
    
    print(f"Area: {result_area}")