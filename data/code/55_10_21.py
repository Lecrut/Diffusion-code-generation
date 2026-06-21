class Triangle:
    def __init__(self, sides):
        self.sides = sides

    @property
    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    triangle_types = {
        'equilateral': [3, 3, 3],
        'isosceles': [5, 5, 8],
        'scalene': [4, 6, 7]
    }
    triangle = Triangle(triangle_types['scalene'])
    print(triangle.perimeter)