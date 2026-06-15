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
        return f"Box(x={self.x}, y={self.y}, z={self.z}, l={self.length}, w={self.width}, h={self.height})"
    def __eq__(self, other):
        if not isinstance(other, Box):
            return NotImplemented
        return (self._x == other._x and self._y == other._y and self._z == other._z and
                self._length == other._length and self._width == other._width and self._height == other._height)
    def __hash__(self):
        return hash((self._x, self._y, self._z, self._length, self._width, self._height))
    def __add__(self, other):
        if not isinstance(other, Box):
            return NotImplemented
        new_x = self._x + other._x
        new_y = self._y + other._y
        new_z = self._z + other._z
        new_l = self._length + other._length
        new_w = self._width + other._width
        new_h = self._height + other._height
        return Box(new_x, new_y, new_z, new_l, new_w, new_h)
    def __sub__(self, other):
        if not isinstance(other, Box):
            return NotImplemented
        new_x = self._x - other._x
        new_y = self._y - other._y
        new_z = self._z - other._z
        new_l = self._length - other._length
        new_w = self._width - other._width
        new_h = self._height - other._height
        return Box(new_x, new_y, new_z, new_l, new_w, new_h)
if __name__ == '__main__':
    box1 = Box(0, 0, 0, 10, 5, 2)
    box2 = Box(3, 4, 1, 4, 6, 3)
    box3 = Box(1, 1, 1, 2, 2, 2)
    print(box1)
    print(box2)
    print(box3)
    box_sum = box1 + box2
    print("\nBox 1 + Box 2:")
    print(box_sum)
    box_diff = box1 - box3
    print("\nBox 1 - Box 3:")
    print(box_diff)