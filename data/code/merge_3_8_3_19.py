def calculate_rectangle_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle given its length and width."""
    return length * width

if __name__ == '__main__':
    # Hard-coded sample values to avoid interactive input requirements.
    try:
        length = 5.0
        width = 3.0
        
        result = calculate_rectangle_area(length, width)
        
        print(f"Rectangle area with dimensions {length} and {width}: {result}")
    except ValueError as e:
        # This block handles cases where input might be non-numeric if run interactively later,
        # though the sample values above are numeric.
        print("Error:", str(e))