class CalculationUtils:
    @staticmethod
    def calculate_rectangle_perimeter(length, width):
        return 2 * (length + width)

if __name__ == '__main__':
    rectangle_length = 8
    rectangle_width = 6

    calculator = CalculationUtils()
    perimeter = calculator.calculate_rectangle_perimeter(rectangle_length, rectangle_width)
    print(perimeter)