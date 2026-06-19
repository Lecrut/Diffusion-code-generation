class Polygon:

    def __init__(self, sides):
        if not all((isinstance(side, (int, float)) and side > 0 for side in sides)):
            raise ValueError('All sides must be positive numbers.')
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)
if __name__ == '__main__':
    try:
        polygon1 = Polygon([3, 4, 5])
        print(polygon1.perimeter())
        polygon2 = Polygon([7, 8, 9, 10])
        print(polygon2.perimeter())
        invalid_polygon = Polygon([-1, 2, 3])
    except ValueError as e:
        print(e)