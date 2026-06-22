class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def get_polygon_type(self):
        num_sides = len(self.sides)
        if num_sides == 3:
            return "Triangle"
        elif num_sides == 4:
            return "Quadrilateral"
        else:
            return f"{num_sides}-sided polygon"

    def calculate_semi_perimeter(self):
        return sum(self.sides) / 2

if __name__ == '__main__':
    sides_triangle = [3, 4, 5]
    triangle = Polygon(sides_triangle)
    print(triangle.get_polygon_type())
    print("Semi-perimeter:", triangle.calculate_semi_perimeter())

    sides_quadrilateral = [2, 3, 4, 5]
    quadrilateral = Polygon(sides_quadrilateral)
    print(quadrilateral.get_polygon_type())
    print("Semi-perimeter:", quadrilateral.calculate_semi_perimeter())