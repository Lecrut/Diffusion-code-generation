class RightAngledTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_hypotenuse(self):
        return (self.base**2 + self.height**2)**0.5

    def calculate_area(self):
        return 0.5 * self.base * self.height

def is_valid_triangle_sides(base, height):
    if base <= 0 or height <= 0:
        return False
    return True

if __name__ == '__main__':
    base = 6.0
    height = 8.0
    
    if is_valid_triangle_sides(base, height):
        triangle = RightAngledTriangle(base, height)
        hypotenuse = triangle.calculate_hypotenuse()
        area = triangle.calculate_area()
        print(f"Hypotenuse: {hypotenuse}")
        print(f"Area: {area}")
    else:
        print("Invalid triangle sides")