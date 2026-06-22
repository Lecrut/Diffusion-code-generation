def triangle_area(p1, p2, p3):
    return abs((p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1])) / 2.0)

class Triangle:
    def __init__(self, points):
        self.points = points
    
    def area(self):
        return triangle_area(*self.points)
    
    def has_equal_area(self, other):
        return self.area() == other.area()

if __name__ == '__main__':
    triangle1 = Triangle(((0, 0), (4, 0), (2, 3)))
    triangle2 = Triangle(((-2, -3), (2, -3), (0, 0)))
    print(triangle1.has_equal_area(triangle2))