class Polygon:
    MIN_SIDES = 3

    def __init__(self, sides):
        if len(sides) < self.MIN_SIDES:
            raise ValueError("A polygon must have at least 3 sides.")
        self.sides = sides
        self.semi_perimeter = sum(self.sides) / 2

    @staticmethod
    def get_polygon_type(num_sides):
        polygon_names = {
            3: "Triangle",
            4: "Quadrilateral"
        }
        return polygon_names.get(num_sides, f"{num_sides}-sided polygon")

    def determine_type_and_semi_perimeter(self):
        num_sides = len(self.sides)
        polygon_type = self.get_polygon_type(num_sides)
        return polygon_type, self.semi_perimeter

if __name__ == '__main__':
    sides_triangle = [3, 4, 5]
    sides_quadrilateral = [2, 2, 3, 3]
    sides_pentagon = [1, 2, 3, 4, 5]

    triangle = Polygon(sides_triangle)
    quadrilateral = Polygon(sides_quadrilateral)
    pentagon = Polygon(sides_pentagon)

    print(triangle.determine_type_and_semi_perimeter())
    print(quadrilateral.determine_type_and_semi_perimeter())
    print(pentagon.determine_type_and_semi_perimeter())