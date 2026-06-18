class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = 0
    
    def is_x_zero(self) -> bool:
        """Checks if instance attribute 'x' is equal to zero."""
        return self.x == 0

if __name__ == '__main__':
    v1 = Vector(5, 3)
    v2 = Vector(0, 7)
    
    print(f"v1.x ({v1.x}) is zero: {v1.is_x_zero()}")
    print(f"v2.x ({v2.x}) is zero: {v2.is_x_zero()}")