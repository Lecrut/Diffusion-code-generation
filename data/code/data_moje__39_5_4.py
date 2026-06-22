from dataclasses import dataclass

@dataclass(frozen=True)
class PrismGeometry:
    base_area: float
    height: float

    @property
    def volume(self) -> float:
        if self.base_area <= 0 or self.height <= 0:
            return 0.0
        return self.base_area * self.height

def compute_volume(geom: PrismGeometry) -> float:
    return geom.volume

if __name__ == '__main__':
    geometry = PrismGeometry(base_area=20.0, height=12.5)
    computed_value = compute_volume(geometry)
    print(computed_value)