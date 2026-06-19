class Polygon:
    def __init__(self, sides):
        self.sides = sides

    @staticmethod
    def polygon_type(sides):
        if len(sides) == 3:
            return "Triangle"
        elif len(sides) == 4:
            return "Quadrilateral"
        else:
            return "Polygon"

    def semi_perimeter(self):
        return sum(self.sides) / 2

if __name__ == '__main__':
    triangle_sides = [3, 4, 5]
    quadrilateral_sides = [2, 2, 2, 2]

    triangle = Polygon(triangle_sides)
    quadrilateral = Polygon(quadrilateral_sides)

    print(f"Triangle Type: {Polygon.polygon_type(triangle_sides)}, Semi-perimeter: {triangle.semi_perimeter()}")
    print(f"Quadrilateral Type: {Polygon.polygon_type(quadrilateral_sides)}, Semi-perimeter: {quadrilateral.semi_perimeter()}")