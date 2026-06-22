import math

class CachedProperty:
    def __init__(self, func):
        self.func = func
        self.attr_name = func.__name__

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        value = self.func(obj)
        setattr(obj, self.attr_name, value)
        return value

class RectangularPrism:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def calculate_surface_area(self):
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)

    @property
    def volume(self):
        return self.length * self.width * self.height

    @CachedProperty
    def cached_surface_area(self):
        return self.calculate_surface_area()

    def get_dimensions(self):
        return self.length, self.width, self.height

if __name__ == '__main__':
    prism = RectangularPrism(5, 10, 20)
    area = prism.cached_surface_area
    print(area)
    prism.width = 15
    new_area = prism.cached_surface_area
    print(new_area)