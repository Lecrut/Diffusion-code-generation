class Square:
    """A class representing a square with side length."""

    def __init__(self, side_length: float) -> None:
        if side_length < 0:
            raise ValueError("Side length must be non-negative.")
        
        self._side = side_length
    
    @property
    def area(self) -> float:
        """Returns the area of the square."""
        return self._side ** 2

if __name__ == '__main__':
    # Sample value for testing
    sample_side = 5.0
    
    try:
        sq = Square(sample_side)
        print(f"Square side length: {sq._side}")
        area_value = sq.area
        print(f"Calculated area: {area_value}")
        
        # Test with another value to ensure robustness
        sample_side_2 = 3.0
        sq_2 = Square(sample_side_2)
        expected_area = sample_side_2 ** 2
        assert abs(sq_2.area - expected_area) < float("inf"), "Area calculation failed."
        print(f"Verification passed for side {sample_side_2}")

    except ValueError as ve:
        print(f"Error occurred during initialization or validation: {ve}")