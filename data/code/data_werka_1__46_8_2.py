class Triangle:
    def __init__(self, side_lengths):
        self.sides = side_lengths

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    triangle_sides = {'side1': 6, 'side2': 8, 'side3': 10}
    sides_list = [triangle_sides['side1'], triangle_sides['side2'], triangle_sides['side3']]
    triangle = Triangle(sides_list)
    print(triangle.perimeter())