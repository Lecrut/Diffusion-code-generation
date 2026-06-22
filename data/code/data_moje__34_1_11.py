import math

class Cylinder:
    TWO = 2
    
    def __init__(self, radius: float, height: float):
        if radius <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        self.radius = radius
        self.height = height
    
    def _compute_base_area(self) -> float:
        return math.pi * (self.radius ** 2)
    
    def _compute_lateral_area(self) -> float:
        return 2 * math.pi * self.radius * self.height
    
    def surface_area(self) -> float:
        base = self._compute_base_area()
        lateral = self._compute_lateral_area()
        return self.TWO * base + lateral

if __name__ == '__main__':
    cyl = Cylinder(radius=7, height=14)
    area = cyl.surface_area()
    print(area)