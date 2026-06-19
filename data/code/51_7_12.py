class CalculationUtils:
    @staticmethod
    def calculate_perimeter(length, width):
        return 2 * (length + width)

if __name__ == '__main__':
    rectangle_length = 7
    rectangle_width = 3

    calculator = CalculationUtils()
    perimeter = calculator.calculate_perimeter(rectangle_length, rectangle_width)
    print(perimeter)