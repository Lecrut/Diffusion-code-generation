class RectangleUtility:
    @staticmethod
    def calculate_perimeter(length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        return 2 * (length + width)

if __name__ == '__main__':
    sample_length = 5
    sample_width = 3
    perimeter = RectangleUtility.calculate_perimeter(sample_length, sample_width)
    print(perimeter)