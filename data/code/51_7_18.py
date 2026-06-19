class CalculationUtils:
    @staticmethod
    def calculate_perimeter(length, width):
        perimeter = 2 * (length + width)
        return perimeter

if __name__ == '__main__':
    rectangle_length = 7
    rectangle_width = 2
    calculated_perimeter = CalculationUtils.calculate_perimeter(rectangle_length, rectangle_width)
    print(calculated_perimeter)