import re
from dataclasses import dataclass
@dataclass
class MapColorPair:
    name: str
    color: tuple[int, int, int] | None = None
    @classmethod
    def validate_name(cls, value: str) -> bool:
        return all(c.isalnum() or c in '_-' for c in value) and len(value) > 0
    @classmethod
    def validate_color(cls, value: tuple[int, int, int]) -> bool:
        if not isinstance(value, (tuple, list)):
            return False
        try:
            r = int(value[0])
            g = int(value[1])
            b = int(value[2])
            return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255
        except (ValueError, TypeError):
            return False
    def __post_init__(self) -> None:
        if not self.validate_name(self.name):
            raise ValueError(f"Invalid map name '{self.name}'. Only alphanumeric characters, underscores, hyphens allowed.")
        if not isinstance(self.color, tuple) or len(self.color) != 3:
            raise ValueError("Color must be a valid RGB tuple of integers between 0 and 255.")
if __name__ == '__main__':
    try:
        pair1 = MapColorPair(name="Forest", color=(34, 139, 34))
        print(f"Created {pair1.name}: {pair1.color}")
        try:
            bad_pair = MapColorPair(name="Map@Name!", color=(255, 0, 0))
        except ValueError as e:
            print(f"Caught expected error for bad name: {e}")
        try:
            float_color_map = MapColorPair(name="Ocean", color=(135.2, 206, 235))
        except ValueError as e:
            print(f"Caught expected error for bad color type: {e}")
    except Exception as ex:
        print(f"Unexpected exception occurred during initialization: {ex}")