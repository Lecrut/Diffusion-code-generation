class AreaComparer:
    RECTANGLE = "rectangle"
    TRIANGLE = "triangle"

    @staticmethod
    def calculate_rectangle_area(length, width):
        return length * width

    @staticmethod
    def calculate_triangle_area(base, height):
        return 0.5 * base * height

    @classmethod
    def compare_areas(cls, rect_length, rect_width, tri_base, tri_height):
        rect_area = cls.calculate_rectangle_area(rect_length, rect_width)
        tri_area = cls.calculate_triangle_area(tri_base, tri_height)
        
        if rect_area > tri_area:
            return rect_area, cls.RECTANGLE
        else:
            return tri_area, cls.TRIANGLE

if __name__ == '__main__':
    rect_l = 12
    rect_w = 7
    tri_b = 9
    tri_h = 5
    larger_area, shape = AreaComparer.compare_areas(rect_l, rect_w, tri_b, tri_h)
    print(f"Larger area: {larger_area}")
    print(f"Shape: {shape}")