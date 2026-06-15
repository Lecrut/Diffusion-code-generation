class Shape:
    def calculate_area(self):
        raise NotImplementedError
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def calculate_area(self):
        return self.side * self.side
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def calculate_area(self):
        return 0.5 * self.base * self.height
class ShapeComparator:
    def compare_areas(self, shape1: Shape, shape2: Shape):
        area1 = shape1.calculate_area()
        area2 = shape2.calculate_area()
        if area1 > area2:
            return f"{shape1.__class__.__name__} has a larger area ({area1:.2f} vs {area2:.2f})"
        elif area1 < area2:
            return f"{shape1.__class__.__name__} has a smaller area ({area1:.2f} vs {area2:.2f})"
        else:
            return f"{shape1.__class__.__name__} and {shape2.__class__.__name__} have equal areas ({area1:.2f})"
if __name__ == '__main__':
    square = Square(side=5)
    triangle = Triangle(base=6, height=4)
    comparator = ShapeComparator()
    print(comparator.compare_areas(square, triangle))