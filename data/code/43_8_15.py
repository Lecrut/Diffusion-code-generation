def calculate_square_area(side_length):
    """Calculates the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    sample_side = 5
    
    try:
        calculated_area = calculate_square_area(sample_side)
        print(f"The area of a square with side length {sample_side} is {calculated_area}")
    except Exception as e:
        print(f"An error occurred during calculation: {e}")