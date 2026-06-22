class Parallelogram:
    def __init__(self, base, height):
        if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Base and height must be numeric values")
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive values")
        self._base = base
        self._height = height

    def area(self):
        return self._base * self._height

if __name__ == '__main__':
    shape = Parallelogram(10, 5)
    print(shape.area())