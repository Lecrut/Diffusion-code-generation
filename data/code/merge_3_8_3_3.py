def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle given its length and width."""
    return length * width

if __name__ == '__main__':
    # Sample dimensions hard-coded as per requirements to avoid interactive input
    sample_length = 5.0
    sample_width = 3.0

    try:
        result = calculate_rectangle_area(sample_length, sample_width)
        print(f"Rectangle area with length {sample_length} and width {sample_width}: {result}")
    except ValueError as e:
        # This block would catch errors if inputs were dynamic but remains silent for hard-coded values
        pass