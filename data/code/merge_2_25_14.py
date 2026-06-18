import re
from dataclasses import dataclass
@dataclass
class MapColorPair:
    map_name: str
    color_code: int | tuple[int]
    def __post_init__(self):
        if not self.map_name.strip():
            raise ValueError("Map name cannot be empty.")
        pattern = r'^[A-Z][a-zA-Z0-9_]{2,15}$'
        if not re.match(pattern, self.map_name):
            raise ValueError(f"Invalid map name: '{self.map_name}'. Must start with uppercase letter and contain only alphanumeric characters or underscores.")
        valid_colors = [
            (34, "gray"), (36, "dark gray"), (215, "blue"), 
            (70, "green"), (98, "cyan"), (212, "yellow")
        ]
        if isinstance(self.color_code, int):
            try:
                color_name = next((c[0] for c in valid_colors if self.color_code == c), None) or hex(self.color_code)[3:]
            except StopIteration:
                raise ValueError(f"Invalid integer color code {self.color_code}. Only specific colors allowed.")
        elif isinstance(self.color_code, tuple):
            try:
                r = int(self.color_code[0])
                g = int(self.color_code[1])
                b = int(self.color_code[2])
                if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
                    raise ValueError("RGB values must be between 0 and 255.")
            except TypeError:
                raise ValueError(f"Invalid RGB tuple {self.color_code}.")
        self._color_name = color_name
if __name__ == '__main__':
    try:
        pair1 = MapColorPair(map_name="NorthAmerica", color_code=34)
        print(f"Created Pair 1: Name={pair1.map_name}, Color Code={hex(pair1.color_code)}")
        pair2 = MapColorPair(
            map_name="_CentralAsia_", 
            color_code=(50, 50, 50)
        )
        print(f"Created Pair 2: Name={pair2.map_name}, RGB Tuple={pair2.color_code}")
    except ValueError as e:
        print(f"Validation Error: {e}")