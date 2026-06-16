import re
from dataclasses import dataclass
@dataclass
class MapColorPair:
    name: str
    color: str
    def __post_init__(self):
        if not self.name.strip():
            raise ValueError("Map name cannot be empty.")
        pattern = r'^[a-zA-Z][a-zA-Z0-9_\-]*$'
        if not re.match(pattern, self.name):
            raise ValueError(f"Invalid map name '{self.name}'. Must start with a letter and contain only letters, numbers, underscores, or hyphens.")
        valid_colors = {
            'red', 'green', 'blue', 'yellow', 
            'orange', 'purple', 'pink', 'brown', 
            'black', 'white', 'gray'
        }
        if self.color.lower() not in valid_colors:
            raise ValueError(f"Invalid color '{self.color}'. Must be one of {valid_colors}.")
if __name__ == '__main__':
    try:
        pair1 = MapColorPair(name="North_America", color='green')
        print("Map:", pair1.name, "Color:", pair1.color)
        try:
            bad_pair = MapColorPair(name="123Start", color='red')
        except ValueError as e:
            print("Error creating bad pair:", str(e))
    except Exception as ex:
        print("Unexpected error:", ex)