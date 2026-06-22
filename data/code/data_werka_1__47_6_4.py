class TriangleCalculator:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3

    def calculate_area(self):
        try:
            area = abs((self.x1 * (self.y2 - self.y3) +
                        self.x2 * (self.y3 - self.y1) +
                        self.x3 * (self.y1 - self.y2)) / 2.0)
            if area < 0:
                raise ValueError("Invalid triangle vertices")
            return area
        except TypeError:
            raise ValueError("Coordinates must be numbers")

if __name__ == '__main__':
    try:
        t = TriangleCalculator(0, 0, 4, 0, 2, 3)
        area = t.calculate_area()
        print(area)
    except ValueError as e:
        print(e)