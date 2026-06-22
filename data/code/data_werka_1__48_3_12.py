import math

class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1, self.y1 = (x1, y1)
        self.x2, self.y2 = (x2, y2)
        self.x3, self.y3 = (x3, y3)

    def side_length(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def calculate_sides(self):
        side1 = self.side_length(self.x1, self.y1, self.x2, self.y2)
        side2 = self.side_length(self.x2, self.y2, self.x3, self.y3)
        side3 = self.side_length(self.x3, self.y3, self.x1, self.y1)
        return (side1, side2, side3)
if __name__ == '__main__':
    triangle = Triangle(0, 0, 3, 4, 6, 0)
    sides = triangle.calculate_sides()
    print(sides)