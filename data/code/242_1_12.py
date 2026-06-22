class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3

    def area(self):
        return abs((self.x1*(self.y2-self.y3) + self.x2*(self.y3-self.y1) + self.x3*(self.y1-self.y2)) / 2.0)

if __name__ == '__main__':
    triangle = Triangle(0, 0, 4, 0, 0, 3)
    print(triangle.area())