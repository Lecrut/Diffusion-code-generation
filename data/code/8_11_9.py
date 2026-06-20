import math
from typing import List, Tuple

SCALE_FACTOR_MIN = 0.001
MAX_SHAPES = 100

class GeometricEntity:
    def calculate_area(self) -> float:
        raise ValueError("Direct instantiation of GeometricEntity is not supported")
    
    def resize(self, multiplier: float) -> None:
        if multiplier <= SCALE_FACTOR_MIN:
            raise ValueError(f"Multiplier must be greater than {SCALE_FACTOR_MIN}")

class Disk(GeometricEntity):
    def __init__(self, radius: float) -> None:
        self.radius = radius
    
    def calculate_area(self) -> float:
        return math.pi * self.radius * self.radius
    
    def resize(self, multiplier: float) -> None:
        super().resize(multiplier)
        self.radius *= multiplier
    
    def describe(self) -> str:
        return f"Disk with radius {self.radius:.2f} and area {self.calculate_area():.2f}"

class Box(GeometricEntity):
    def __init__(self, length: float, width: float, height: float) -> None:
        self.length = length
        self.width = width
        self.height = height
    
    def calculate_area(self) -> float:
        return 2 * (self.length * self.width + self.width * self.height + self.height * self.length)
    
    def resize(self, multiplier: float) -> None:
        super().resize(multiplier)
        self.length *= multiplier
        self.width *= multiplier
        self.height *= multiplier
    
    def describe(self) -> str:
        return f"Box with dims {self.length:.2f}x{self.width:.2f}x{self.height:.2f} and area {self.calculate_area():.2f}"

def process_shapes(items: List[GeometricEntity], factor: float) -> List[float]:
    results: List[float] = []
    for item in items:
        old_area = item.calculate_area()
        item.resize(factor)
        new_area = item.calculate_area()
        results.append(new_area)
    return results

if __name__ == '__main__':
    shape_registry: List[GeometricEntity] = [
        Disk(5.0),
        Box(2.0, 3.0, 4.0),
        Disk(10.0),
        Box(1.0, 1.0, 1.0)
    ]
    scaling_factor = 2.0
    final_areas = process_shapes(shape_registry, scaling_factor)
    print(f"Original shape count: {len(shape_registry)}")
    print(f"Applied scaling factor: {scaling_factor}")
    for idx, area in enumerate(final_areas):
        print(f"Shape {idx + 1} new area: {area:.4f}")