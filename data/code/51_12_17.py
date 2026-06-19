class Shape:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def calculate_perimeter(self):
        return sum(dimensions)

if __name__ == '__main__':
    rectangle_dimensions1 = [5, 10]
    shape1 = Shape(rectangle_dimensions1)
    perimeter1 = shape1.calculate_perimeter()
    print(perimeter1)

    rectangle_dimensions2 = [7, 3]
    shape2 = Shape(rectangle_dimensions2)
    perimeter2 = shape2.calculate_perimeter()
    print(perimeter2)