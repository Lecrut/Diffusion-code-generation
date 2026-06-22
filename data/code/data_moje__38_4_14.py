import math
from dataclasses import dataclass

@dataclass
class ConeGeometry:
    radius: float
    height: float

    def validate_positive(self) -> None:
        if self.radius <= 0 or self.height <= 0:
            raise ValueError("Dimensions must be positive")

    def calculate_volume(self) -> float:
        self.validate_positive()
        base_area = math.pi * (self.radius ** 2)
        volume = base_area * self.height
        return volume / 3.0

if __name__ == '__main__':
    cone = ConeGeometry(radius=6, height=9)
    volume = cone.calculate_volume()
    print(volume)