class AreaComparator:
    RECTANGLE = "rectangle"
    TRIANGLE = "triangle"

    @staticmethod
    def calculate_rectangle_area(length, width):
        return length * width

    @staticmethod
    def calculate_triangle_area(base, height):
        return 0.5 * base * height

    @staticmethod
    def compare_areas(rect_length, rect_width, tri_base, tri_height):
        rect_area = AreaComparator.calculate_rectangle_area(rect_length, rect_width)
        tri_area = AreaComparator.calculate_triangle_area(tri_base, tri_height)

        if rect_area > tri_area:
            return rect_area, AreaComparator.RECTANGLE
        else:
            return tri_area, AreaComparator.TRIANGLE

if __name__ == '__main__':
    rect_l = 7
    rect_w = 3
    tri_b = 6
    tri_h = 5
    larger_area, shape = AreaComparator.compare_areas(rect_l, rect_w, tri_b, tri_h)
    print(f"Larger area: {larger_area}")
    print(f"Corresponding shape: {shape}")