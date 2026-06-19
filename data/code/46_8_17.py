class Triangle:
    def __init__(self, side_lengths):
        self.side_lengths = side_lengths

    def perimeter(self):
        return sum(self.side_lengths)

if __name__ == '__main__':
    triangle_sides = {'side1': 9, 'side2': 12, 'side3': 15}
    sides_list = [triangle_sides['side1'], triangle_sides['side2'], triangle_sides['side3']]
    triangle = Triangle(sides_list)
    print(triangle.perimeter())