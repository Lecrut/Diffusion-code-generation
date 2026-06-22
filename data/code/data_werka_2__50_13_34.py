class RectangleAreaCalculator:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def calculate_area(self, rect_name):
        length = self.dimensions[rect_name]['length']
        width = self.dimensions[rect_name]['width']
        return length * width

    def find_difference(self):
        area1 = self.calculate_area('rectangle1')
        area2 = self.calculate_area('rectangle2')
        return abs(area1 - area2)

if __name__ == '__main__':
    dimensions = {
        'rectangle1': {'length': 5, 'width': 3},
        'rectangle2': {'length': 4, 'width': 6}
    }
    calculator = RectangleAreaCalculator(dimensions)
    difference = calculator.find_difference()
    print(difference)