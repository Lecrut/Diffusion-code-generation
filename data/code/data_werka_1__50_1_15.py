class AreaCalculator:
    def __init__(self, area1, area2):
        self.area1 = area1
        self.area2 = area2

    def calculate_difference(self):
        return abs(self.area1 - self.area2)

if __name__ == '__main__':
    areas = {'room': 50, 'garden': 200}
    calculator = AreaCalculator(areas['room'], areas['garden'])
    difference = calculator.calculate_difference()
    print(difference)