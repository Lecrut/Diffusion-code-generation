from dataclasses import dataclass
from typing import Final

@dataclass(frozen=True)
class RectangularBox:
    length: float
    width: float
    height: float
    MULTIPLIER: Final[float] = 2.0

    @staticmethod
    def compute_surface_area(l: float, w: float, h: float) -> float:
        return RectangularBox.MULTIPLIER * (l * w + w * h + h * l)

    def get_surface_area(self) -> float:
        return self.compute_surface_area(self.length, self.width, self.height)

if __name__ == '__main__':
    box: RectangularBox = RectangularBox(
        length=2.5,
        width=3.0,
        height=4.0,
    )
    area: float = box.get_surface_area()
    print(area)