class Triangle:

    def __init__(self, sides):
        if any((side <= 0 for side in sides)):
            raise ValueError('Sides must be positive numbers.')
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)
if __name__ == '__main__':
    triangle_sides = [3.0, 4.0, 5.0]
    try:
        triangle = Triangle(triangle_sides)
        print('Perimeter:', triangle.perimeter())
    except ValueError as e:
        print(e)