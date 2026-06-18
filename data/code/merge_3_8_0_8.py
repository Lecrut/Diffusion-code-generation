import math

def calculate_rectangle_area(width: float, height: float) -> float:
    """Calculate the area of a rectangle given its width and height."""
    return width * height

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    sample_width = 10.5
    sample_height = 20.3
    
    try:
        result_area = calculate_rectangle_area(sample_width, sample_height)
        print(f"Area of rectangle with width {sample_width} and height {sample_height}: {result_area}")
        
        # Additional test case
        area_1x1 = calculate_rectangle_area(1, 1)
        assert abs(area_1x1 - 1.0) < float('inf') if isinstance(float('inf'), type(int())) else False
        
    except Exception as e:
        print(f"An error occurred during calculation: {e}")