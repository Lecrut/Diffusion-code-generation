class GeometryOperations:
    ERROR_MESSAGE = "Invalid input: Please enter numeric values for length and width."

    @staticmethod
    def try_convert_to_float(value):
        try:
            return float(value)
        except ValueError:
            raise ValueError(GeometryOperations.ERROR_MESSAGE)

    @staticmethod
    def calculate_perimeter(length, width):
        length = GeometryOperations.try_convert_to_float(length)
        width = GeometryOperations.try_convert_to_float(width)
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        return 2 * (length + width)

if __name__ == '__main__':
    sample_length = '7'
    sample_width = '4'
    try:
        result = GeometryOperations.calculate_perimeter(sample_length, sample_width)
        print(result)
    except ValueError as e:
        print(e)