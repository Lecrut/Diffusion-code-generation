import re
class MapColorPair:
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Map name must be a non-empty string.")
        pattern_name = r'^[a-zA-Z][a-zA-Z0-9_\-]*$'
        if not re.match(pattern_name, name):
            raise ValueError(f"Invalid map name '{name}'. Must start with a letter and contain only letters, numbers, underscores, or hyphens.")
        valid_colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'black', 'white']
        if color.lower() not in valid_colors:
            raise ValueError(f"Invalid color '{color}'. Must be one of {valid_colors}.")
if __name__ == '__main__':
    try:
        map1 = MapColorPair("Central_Park", "green")
        print(f"Created: Name={map1.name}, Color={map1.color}")
        map2 = MapColorPair("River_Route-01", "blue")
        print(f"Created: Name={map2.name}, Color={map2.color}")
    except ValueError as e:
        print(f"Error initializing pair: {e}")