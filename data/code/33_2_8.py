class GeometryTriangle:
    _AREA_FACTOR = 0.5

    def __init__(self, base: float, height: float) -> None:
        self._base = base
        self._height = height

    def get_area(self) -> float:
        return self._AREA_FACTOR * self._base * self._height

    def get_dimensions(self) -> tuple:
        return self._base, self._height

if __name__ == '__main__':
    SAMPLE_BASE = 12.5
    SAMPLE_HEIGHT = 8.0
    shape = GeometryTriangle(SAMPLE_BASE, SAMPLE_HEIGHT)
    print(shape.get_area())