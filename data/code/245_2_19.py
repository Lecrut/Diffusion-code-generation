class Triangle:
    @staticmethod
    def area(p1, p2, p3):
        return abs((p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1])) / 2.0)
    
    def __init__(self, points):
        self.points = points
    
    def get_area(self):
        return Triangle.area(*self.points)
    
    @staticmethod
    def are_areas_equal(t1, t2):
        return t1.get_area() == t2.get_area()

if __name__ == '__main__':
    triangle1 = Triangle(((0, 0), (4, 0), (2, 3)))
    triangle2 = Triangle(((-2, -3), (2, -3), (0, 0)))
    print(Triangle.are_areas_equal(triangle1, triangle2))