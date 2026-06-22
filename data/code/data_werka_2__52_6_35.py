import math

class Shape:
    SHAPE_AREA_FUNCTIONS = {
        'rectangle': lambda length, width: length * width,
        'circle': lambda radius: math.pi * radius ** 2
    }

    def __init__(self, shape_type, **dimensions):
        self.shape_type = shape_type.lower()
        self.dimensions = dimensions

    def area(self):
        area_function = self.SHAPE_AREA_FUNCTIONS.get(self.shape_type)
        if area_function:
            required_dimensions = {'rectangle': ('length', 'width'), 'circle': ('radius')}
            for dim in required_dimensions[self.shape_type]:
                if dim not in self.dimensions:
                    raise ValueError(f"{self.shape_type.capitalize()} requires a {dim}")
            return area_function(**self.dimensions)
        else:
            raise ValueError(f"Unsupported shape type: {self.shape_type}")

if __name__ == '__main__':
    rectangle = Shape('rectangle', length=5, width=3)
    circle = Shape('circle', radius=4)

    print("Rectangle Area:", rectangle.area())
    print("Circle Area:", circle.area())