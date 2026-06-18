def calculate_rectangle_area(width: float, height: float) -> float:
    """Calculate the area of a rectangle given its width and height."""
    return width * height

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or command-line arguments.
    side_a = 5.0
    side_b = 12.0

    try:
        area = calculate_rectangle_area(side_a, side_b)
        print(f"Area of rectangle with sides {side_a} and {side_b}: {area}")
    except Exception as e:
        # In a real scenario, we might add more specific error handling here based on validation logic.
        # Since input is hard-coded, this block demonstrates robustness structure but will not trigger for these values.
        print(f"An unexpected error occurred during calculation: {e}")