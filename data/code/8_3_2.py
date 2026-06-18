def calculate_rectangle_area(length: float, width: float) -> float:
    """Calculates the area of a rectangle given its length and width."""
    return length * width

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user input or network access.
    hard_code_length = 5.0
    hard_code_width = 3.0

    try:
        area = calculate_rectangle_area(hard_code_length, hard_code_width)
        print(f"The area of the rectangle is {area}.")
    except Exception as e:
        # This block catches any unexpected errors during calculation.
        print(f"An error occurred while calculating the area: {e}")