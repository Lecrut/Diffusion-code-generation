class Triangle:
    def __init__(self, side_lengths):
        self.sides = {key: length for key, length in zip(('side1', 'side2', 'side3'), side_lengths)}

    def perimeter(self):
        return sum(self.sides.values())

if __name__ == '__main__':
    triangle_sides = {'side1': 9, 'side2': 12, 'side3': 15}
    sides_list = [triangle_sides['side1'], triangle_sides['side2'], triangle_sides['side3']]
    triangle = Triangle(sides_list)
    print(triangle.perimeter())