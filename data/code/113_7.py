class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def subtract(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)
if __name__ == '__main__':
    v1 = Vector(10, 5)
    v2 = Vector(3, 7)
    v3 = v1.subtract(v2)
    print(f"v1: ({v1.x}, {v1.y})")
    print(f"v2: ({v2.x}, {v2.y})")
    print(f"v3 (v1 - v2): ({v3.x}, {v3.y})")