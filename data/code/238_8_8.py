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
    def copy(self):
        return Box(self._position, self._dimensions)
if __name__ == '__main__':
    box1 = Box(position=(1, 2, 3), dimensions=(10, 5, 2))
    box2 = Box((1, 2, 3), (10, 5, 2))
    box3 = Box((4, 5, 6), (8, 4, 3))
    print(box1)
    print(box2)
    print(box3)
    print(f"Box1 == Box2: {box1 == box2}")
    print(f"Box1 == Box3: {box1 == box3}")
    box1_copy = box1.copy()
    print(box1_copy)
    print(f"Box1 == Box1_copy: {box1 == box1_copy}")