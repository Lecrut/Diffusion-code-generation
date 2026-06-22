class Rectangle:
    MIN_DIMENSION = 0

    @staticmethod
    def validate_dimension(value):
        try:
            dimension = float(value)
            if dimension <= Rectangle.MIN_DIMENSION:
                raise ValueError("Dimension must be greater than zero.")
            return dimension
        except ValueError as e:
            return str(e)

    @staticmethod
    def calculate_perimeter(length, width):
        length_val = Rectangle.validate_dimension(length)
        width_val = Rectangle.validate_dimension(width)
        
        if isinstance(length_val, str) or isinstance(width_val, str):
            return "Invalid input: Please enter numeric values for length and width."
        
        perimeter = 2 * (length_val + width_val)
        return perimeter

if __name__ == '__main__':
    sample_length = '7'
    sample_width = '3'
    result = Rectangle.calculate_perimeter(sample_length, sample_width)
    print(result)