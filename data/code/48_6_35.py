class Polygon:
    def __init__(self, sides):
        if len(sides) < 3:
            raise ValueError("A polygon must have at least 3 sides.")
        self.sides = sides
        self.num_sides = len(sides)
        self.semi_perimeter = sum(sides) / 2

    def get_polygon_type(self):
        polygon_types = {
            3: "Triangle",
            4: "Quadrilateral"
        }
        return polygon_types.get(self.num_sides, f"{self.num_sides}-sided polygon")

    def get_semi_perimeter(self):
        return self.semi_perimeter

if __name__ == '__main__':
    sides_triangle = [3, 4, 5]
    sides_quadrilateral = [2, 2, 3, 3]
    sides_pentagon = [1, 2, 3, 4, 5]

    triangle = Polygon(sides_triangle)
    print(f"Polygon type: {triangle.get_polygon_type()}, Semi-perimeter: {triangle.get_semi_perimeter()}")

    quadrilateral = Polygon(sides_quadrilateral)
    print(f"Polygon type: {quadrilateral.get_polygon_type()}, Semi-perimeter: {quadrilateral.get_semi_perimeter()}")

    pentagon = Polygon(sides_pentagon)
    print(f"Polygon type: {pentagon.get_polygon_type()}, Semi-perimeter: {pentagon.get_semi_perimeter()}")