from dataclasses import dataclass
from typing import final

FACTOR_TWO: final = 2

@dataclass
class RectangularBox:
    length: float
    width: float
    height: float

    def compute_surface_area(self) -> float:
        area_lw: float = self.length * self.width
        area_wh: float = self.width * self.height
        area_hl: float = self.height * self.length
        return FACTOR_TWO * (area_lw + area_wh + area_hl)

if __name__ == '__main__':
    box_instance: RectangularBox = RectangularBox(length=2.5, width=3.0, height=4.0)
    total_area: float = box_instance.compute_surface_area()
    print(total_area)