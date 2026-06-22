class RhombusAreaCalculator:
    @staticmethod
    def calculate_area(diagonal1, diagonal2):
        return (diagonal1 * diagonal2) / 2

def calculate_total_area():
    rhombus1 = RhombusAreaCalculator.calculate_area(6, 8)
    rhombus2 = RhombusAreaCalculator.calculate_area(10, 12)
    return rhombus1 + rhombus2

if __name__ == '__main__':
    result = calculate_total_area()
    print(result)