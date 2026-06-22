def shoelace_area(coords):
    n = len(coords)
    area = 0.5 * abs(sum(x1*y2 - x2*y1 for (x1, y1), (x2, y2) in zip(coords, coords[1:] + coords[:1])))
    return area

class Polygon:
    SHOELACE = 'shoelace'

    @staticmethod
    def calculate_area(coords):
        return shoelace_area(coords)

if __name__ == '__main__':
    polygon1_coords = [(0, 0), (4, 0), (4, 3), (0, 3)]
    polygon2_coords = [(5, 0), (9, 0), (9, 4), (5, 4)]

    area1 = Polygon.calculate_area(polygon1_coords)
    area2 = Polygon.calculate_area(polygon2_coords)

    print(f"Area of polygon 1: {area1}")
    print(f"Area of polygon 2: {area2}")
    print(f"Do the polygons have equal area? {'Yes' if area1 == area2 else 'No'}")