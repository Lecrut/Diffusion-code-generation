"""Module to calculate area based on length and width."""

def calculate_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle given its length and width.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The calculated area as an integer or float depending on input types, 
               but typically cast to int if both inputs are integers in this specific optimized version logic for simplicity, 
               however adhering strictly to type hints which imply return matches sum/product logic usually yielding same type. 
               Here returning the mathematical product directly.
    """
    area = length * width
    return area

if __name__ == '__main__':
    sample_length = 5
    sample_width = 10
    result_area = calculate_area(sample_length, sample_width)
    print(f"The area is: {result_area}")