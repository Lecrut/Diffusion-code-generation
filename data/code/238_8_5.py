class Box:
    def __init__(self, x, y, z, length, width, height):
        self._x = x
        self._y = y
        self._z = z
        self._length = length
        self._width = width
        self._height = height
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @property
    def z(self):
        return self._z
    @property
    def length(self):
        return self._length
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    def __repr__(self):
        return f"Box(x={self._x}, y={self._y}, z={self._z}, l={self._length}, w={self._width}, h={self._height})"
    def translate(self, dx, dy, dz):
        new_x = self._x + dx
        new_y = self._y + dy
        new_z = self._z + dz
        return Box(new_x, new_y, new_z, self._length, self._width, self._height)
    def scale(self, factor):
        new_length = self._length * factor
        new_width = self._width * factor
        new_height = self._height * factor
        return Box(self._x, self._y, self._z, new_length, new_width, new_height)
if __name__ == '__main__':
    box1 = Box(0, 0, 0, 10, 5, 2)
    print(f"Original Box: {box1}")
    box2 = box1.translate(3, -1, 5)
    print(f"Translated Box: {box2}")
    box3 = box1.scale(2.5)
    print(f"Scaled Box: {box3}")
    box4 = Box(100, 200, 300, 1, 1, 1)
    print(f"New Independent Box: {box4}")