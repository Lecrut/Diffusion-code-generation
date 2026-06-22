import math
from dataclasses import dataclass
from typing import Dict

SHAPE_CONFIGS: Dict[str, float] = {"cone": 1.0 / 3.0}

@dataclass
class GeometricSolid:
    radius: float
    height: float
    shape_type: str

    def compute_volume(self) -> float:
        coefficient = SHAPE_CONFIGS[self.shape_type]
        base_area = math.pi * (self.radius ** 2)
        return coefficient * base_area * self.height

if __name__ == '__main__':
    DIMENSIONAL_DATA = {"radius": 5.0, "height": 10.0, "type": "cone"}
    solid_instance = GeometricSolid(
        radius=5.0,
        height=10.0,
        shape_type="cone"
    )
    result_volume = solid_instance.compute_volume()
    print(result_volume)