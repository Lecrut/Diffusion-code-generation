class PerimeterCalculator:
    @staticmethod
    def calculate_perimeter(sides):
        return sum(sides)

if __name__ == '__main__':
    sample_sides = [7, 8, 9, 10]
    perimeter = PerimeterCalculator.calculate_perimeter(sample_sides)
    print(perimeter)