class GeometryUtils:
    @staticmethod
    def calculate_area(shape, *args):
        if shape == 'rectangle':
            length, width = args
            return length * width
        elif shape == 'circle':
            radius = args[0]
            import math
            return math.pi * (radius ** 2)
        elif shape == 'triangle':
            base, height = args
            return 0.5 * base * height
        else:
            raise ValueError("Unsupported shape")

if __name__ == '__main__':
    rectangle_area = GeometryUtils.calculate_area('rectangle', 5, 10)
    circle_area = GeometryUtils.calculate_area('circle', 7)
    triangle_area = GeometryUtils.calculate_area('triangle', 4, 6)

    print(f"Rectangle Area: {rectangle_area}")
    print(f"Circle Area: {circle_area}")
    print(f"Triangle Area: {triangle_area}")