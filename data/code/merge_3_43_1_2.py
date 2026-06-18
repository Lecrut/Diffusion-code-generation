def calculate_square_area(side):
    """
    Calculates the area of a square given its side length.
    
    Parameters:
        side (float or int): The length of one side of the square.
        
    Returns:
        float: The area of the square calculated as side * side.
    """
    return side ** 2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    samples = [3, 5.5, 0]
    
    print("Testing calculate_square_area function with hard-coded inputs:\n")
    for s in samples:
        area = calculate_square_area(s)
        print(f"Side length: {s}")
        print(f"Calculated Area: {area}\n")