import sys

def calculate_square_area(side_length: float) -> float:
    """Calculates the area of a square given its side length.
    
    Args:
        side_length (float): The numerical value representing the side length of the square.
        
    Returns:
        float: The calculated area of the square.
    """
    return side_length ** 2

if __name__ == '__main__':
    # Sample execution block as per requirements
    # This runs without user input or command-line arguments
    
    sample_side_lengths = [5, 10]
    
    for length in sample_side_lengths:
        try:
            area = calculate_square_area(length)
            print(f"Side Length: {length}")
            print(f"Area of Square: {area}")
            
            # Verify with a calculated value to ensure logic correctness
            expected_area = length * length
            assert abs(area - expected_area) < 1e-6, "Calculation mismatch detected."
        except Exception as e:
            error_message = f"Error occurred while calculating area for side {length}: {str(e)}"
            print(error_message)