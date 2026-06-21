import math

class Geometry:
    SHAPE_AREAS = {
        'rectangle': lambda length, width: length * width,
        'circle': lambda radius: math.pi * radius ** 2,
        'triangle': lambda base, height: 0.5 * base * height
    }

    def area(self, shape, *args):
        if shape in self.SHAPE_AREAS:
            return self.SHAPE_AREAS[shape](*args)
        else:
            raise ValueError("Unsupported shape")

if __name__ == '__main__':
    geometry = Geometry()
    rectangle_area = geometry.area('rectangle', 6, 4)
    circle_area = geometry.area('circle', 5)
    triangle_area = geometry.area('triangle', 9, 3)
    print(f"Rectangle Area: {rectangle_area}")
    print(f"Circle Area: {circle_area}")
    print(f"Triangle Area: {triangle_area}")