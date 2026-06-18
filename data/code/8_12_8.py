class GeometryCalculator:
    """A utility class to perform basic geometric calculations."""

    def calculate_area_of_rectangle(self, length: float, width: float) -> float:
        """Calculates the area of a rectangle given its length and width.
        
        Args:
            length (float): The length of the rectangle in arbitrary units.
            width (float): The width of the rectangle in arbitrary units.
            
        Returns:
            float: The calculated area as the product of length and width.
            
        Raises:
            TypeError: If either dimension is not a numeric type.
            ValueError: If any dimension is negative.
        
        Example:
            >>> calc = GeometryCalculator()
            >>> print(calc.calculate_area_of_rectangle(5, 10))
            50.0
        
        """
        if not isinstance(length, (int, float)):
            raise TypeError(f"Length must be a number, got {type(length).__name__}")
        if not isinstance(width, (int, float)):
            raise TypeError(f"Width must be a number, got {type(width).__name__}")
        
        if length < 0 or width < 0:
            raise ValueError("Length and width cannot be negative.")

        return length * width

if __name__ == '__main__':
    # Hard-coded sample values for demonstration; no user input required.
    calculator = GeometryCalculator()

    l = 12.5
    w = 8.0

    area = calculator.calculate_area_of_rectangle(l, w)

    print(f"Rectangle Area (L={l}, W={w}): {area}")