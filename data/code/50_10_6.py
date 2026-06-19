class AreaCalculator:
    def __init__(self, area1, area2):
        self.area1 = area1
        self.area2 = area2

    def calculate_difference(self):
        try:
            return abs(float(self.area1) - float(self.area2))
        except ValueError:
            raise ValueError("Error: Invalid input. Please enter numeric values.")

if __name__ == '__main__':
    area_calculator = AreaCalculator(150, 225)
    difference = area_calculator.calculate_difference()
    print(difference)