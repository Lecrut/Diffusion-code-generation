class CalculationUtils:
    PERIMETER_FORMULA = "2 * (length + width)"

    @staticmethod
    def calculate_perimeter(length, width):
        return 2 * (length + width)

if __name__ == '__main__':
    length = 7
    width = 2
    perimeter = CalculationUtils.calculate_perimeter(length, width)
    print(perimeter)