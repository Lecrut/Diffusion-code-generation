import math

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3

    def distance(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def side_lengths(self):
        a = self.distance(self.x1, self.y1, self.x2, self.y2)
        b = self.distance(self.x2, self.y2, self.x3, self.y3)
        c = self.distance(self.x3, self.y3, self.x1, self.y1)
        return a, b, c

if __name__ == '__main__':
    triangle = Triangle(0, 0, 3, 4, 6, 0)
    side_lengths = triangle.side_lengths()
    print("Side lengths:", side_lengths)