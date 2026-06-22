import math

class ConeGeometry:
    __slots__ = ("radius", "height")
    _volume_multiplier = math.pi / 3

    def __init__(self, radius: float, height: float):
        if radius <= 0:
            raise ValueError("radius must be positive")
        if height <= 0:
            raise ValueError("height must be positive")
        self.radius = float(radius)
        self.height = float(height)

    def compute_volume(self) -> float:
        return self._volume_multiplier * (self.radius ** 2) * self.height

def format_cone_volume(radius: float, height: float) -> str:
    cone = ConeGeometry(radius, height)
    vol = cone.compute_volume()
    return f"{vol:.2f}"

if __name__ == "__main__":
    result = format_cone_volume(8, 11)
    print(result)