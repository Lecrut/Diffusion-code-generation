class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

class Trapezoid:
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height
    
    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

def calculate_total_area(shapes):
    total_area = 0
    for shape in shapes:
        if isinstance(shape, Triangle):
            total_area += shape.area()
        elif isinstance(shape, Trapezoid):
            total_area += shape.area()
    return total_area

if __name__ == '__main__':
    triangle = Triangle(3, 4)
    trapezoid = Trapezoid(5, 7, 8)
    shapes = [triangle, trapezoid]
    print(calculate_total_area(shapes))