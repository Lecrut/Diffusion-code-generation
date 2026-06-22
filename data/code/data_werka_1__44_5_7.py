class GeometryUtils:
    @staticmethod
    def calculate_perimeter(length, width):
        if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
            raise TypeError("Length and width must be numeric values.")
        perimeter = 2 * (length + width)
        return perimeter

if __name__ == '__main__':
    sample_dimensions_valid = {'length': 10, 'width': 5}
    sample_dimensions_invalid_type = {'length': 10, 'width': "five"}
    
    try:
        perimeter1 = GeometryUtils.calculate_perimeter(sample_dimensions_valid['length'], sample_dimensions_valid['width'])
        print(f"Perimeter for {sample_dimensions_valid}: {perimeter1}")
    except (ValueError, TypeError) as e:
        print(f"Error calculating perimeter for {sample_dimensions_valid}: {e}")

    try:
        perimeter2 = GeometryUtils.calculate_perimeter(sample_dimensions_invalid_type['length'], sample_dimensions_invalid_type['width'])
        print(f"Perimeter for {sample_dimensions_invalid_type}: {perimeter2}")
    except (ValueError, TypeError) as e:
        print(f"Error calculating perimeter for {sample_dimensions_invalid_type}: {e}")