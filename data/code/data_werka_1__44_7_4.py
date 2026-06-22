class GeometryCalculator:
    @staticmethod
    def validate_number(value):
        try:
            num = float(value)
            if num <= 0:
                raise ValueError("The value must be a positive number.")
            return num
        except ValueError as e:
            return str(e)

    @staticmethod
    def calculate_perimeter(length, width):
        length_val = GeometryCalculator.validate_number(length)
        width_val = GeometryCalculator.validate_number(width)
        
        if isinstance(length_val, str) or isinstance(width_val, str):
            return f"Invalid input: {length_val} or {width_val}"
        
        perimeter = 2 * (length_val + width_val)
        return perimeter

if __name__ == '__main__':
    sample_length = "10"
    sample_width = "5"
    result = GeometryCalculator.calculate_perimeter(sample_length, sample_width)
    print(result)