def calculate_rectangle_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle given its length and width."""
    return length * width

if __name__ == '__main__':
    # Hard-coded sample values to avoid interactive input requirements.
    sample_length = 5.0
    sample_width = 3.0

    try:
        area = calculate_rectangle_area(sample_length, sample_width)
        print(f"Area of rectangle with length {sample_length} and width {sample_width}: {area}")
    except ValueError as e:
        # This block handles potential errors if the logic were to accept dynamic input.
        # Since we are using hard-coded values here, this exception is not triggered by default execution flow,
        # but it demonstrates proper error handling structure for non-numeric inputs in a broader context.
        print(f"Error: {e}")