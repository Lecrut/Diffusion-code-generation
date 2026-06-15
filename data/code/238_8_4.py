class Box:
    def __init__(self, position, dimensions):
        self._position = tuple(position)
        self._dimensions = tuple(dimensions)
    @property
    def position(self):
        return self._position
    @property
    def dimensions(self):
        return self._dimensions
    def __repr__(self):
        return f"Box(position={self._position}, dimensions={self._dimensions})"
    def __eq__(self, other):
        if not isinstance(other, Box):
            return NotImplemented
        return self._position == other._position and self._dimensions == other._dimensions
    def __hash__(self):
        return hash((self._position, self._dimensions))
    def __sub__(self, other):
        if not isinstance(other, Box):
            return NotImplemented
        raise TypeError("Subtraction between Box objects is not supported")
    def __add__(self, other):
        if not isinstance(other, Box):
            return NotImplemented
        new_pos = tuple(self._position[i] + other._position[i] for i in range(len(self._position)))
        new_dims = tuple(self._dimensions[i] + other._dimensions[i] for i in range(len(self._dimensions)))
        return Box(new_pos, new_dims)
if __name__ == '__main__':
    box1 = Box((0, 0, 0), (10, 5, 2))
    box2 = Box((5, 5, 5), (3, 4, 1))
    box3 = Box((0, 0, 0), (10, 5, 2))
    print(box1)
    print(box2)
    print(box3)
    print(f"Box1 == Box3: {box1 == box3}")
    print(f"Hash of Box1: {hash(box1)}")
    try:
        box4 = box1 - box2
        print(f"Box1 - Box2: {box4}")
    except TypeError as e:
        print(f"Error during subtraction: {e}")