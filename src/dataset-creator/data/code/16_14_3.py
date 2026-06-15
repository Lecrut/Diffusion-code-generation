class ColorManager:
    def __init__(self):
        self._color_to_rgb = {}
        self._rgb_to_color = {}
    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip('#')
        if len(hex_color) != 6:
            raise ValueError("Invalid hex color format")
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        return r, g, b
    def add_color(self, hex_color, name):
        r, g, b = self.hex_to_rgb(hex_color)
        rgb_tuple = (r, g, b)
        self._color_to_rgb[name] = rgb_tuple
        self._rgb_to_color[rgb_tuple] = name
    def get_color_name_from_rgb(self, r, g, b):
        rgb_tuple = (r, g, b)
        return self._rgb_to_color.get(rgb_tuple, "Unknown")
if __name__ == '__main__':
    manager = ColorManager()
    manager.add_color("#FF0000", "Red")
    manager.add_color("#00FF00", "Green")
    manager.add_color("#0000FF", "Blue")
    manager.add_color("#FFFFFF", "White")
    manager.add_color("#123456", "Custom1")
    print(f"Color mapping (Name to RGB): {manager._color_to_rgb}")
    r, g, b = 255, 0, 0
    name = manager.get_color_name_from_rgb(r, g, b)
    print(f"RGB ({r}, {g}, {b}) maps to: {name}")
    r, g, b = 12, 52, 86
    name = manager.get_color_name_from_rgb(r, g, b)
    print(f"RGB ({r}, {g}, {b}) maps to: {name}")
    r, g, b = 0, 255, 0
    name = manager.get_color_name_from_rgb(r, g, b)
    print(f"RGB ({r}, {g}, {b}) maps to: {name}")
    r, g, b = 10, 20, 30
    name = manager.get_color_name_from_rgb(r, g, b)
    print(f"RGB ({r}, {g}, {b}) maps to: {name}")