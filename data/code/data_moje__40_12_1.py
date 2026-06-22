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

    @CachedProperty
    def surface_area(self):
        l = self.length
        w = self.width
        h = self.height
        return 2 * (l * w + w * h + h * l)

if __name__ == '__main__':
    prism = RectangularPrism(2.0, 3.0, 4.0)
    result = prism.surface_area
    print(result)