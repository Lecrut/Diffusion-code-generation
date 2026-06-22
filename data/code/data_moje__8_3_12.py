class PolygonAreaCalculator:
    MIN_VERTICES = 3
    AREA_DIVISOR = 2.0

    @staticmethod
    def calculate_polygon_area(vertices):
        if len(vertices) < PolygonAreaCalculator.MIN_VERTICES:
            return 0.0
        n = len(vertices)
        cross_sum = 0.0
        for i in range(n):
            current_vertex = vertices[i]
            next_vertex = vertices[(i + 1) % n]
            cross_sum += current_vertex[0] * next_vertex[1]
            cross_sum -= next_vertex[0] * current_vertex[1]
        return abs(cross_sum) / PolygonAreaCalculator.AREA_DIVISOR

    @staticmethod
    def validate_vertices(vertices):
        return len(vertices) >= PolygonAreaCalculator.MIN_VERTICES and all(
            isinstance(v, (list, tuple)) and len(v) == 2 and all(isinstance(coord, (int, float)) for coord in v)
            for v in vertices
        )

if __name__ == '__main__':
    triangle_coords = [(0.0, 0.0), (4.0, 0.0), (0.0, 3.0)]
    rectangle_coords = [(1.0, 1.0), (5.0, 1.0), (5.0, 4.0), (1.0, 4.0)]
    irregular_coords = [(0, 0), (4, 0), (5, 3), (2, 5), (0, 2)]

    print(PolygonAreaCalculator.calculate_polygon_area(triangle_coords))
    print(PolygonAreaCalculator.calculate_polygon_area(rectangle_coords))
    print(PolygonAreaCalculator.calculate_polygon_area(irregular_coords))