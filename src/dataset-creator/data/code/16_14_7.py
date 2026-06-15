class ColorManager:
    def __init__(self):
        self._color_to_rgb = {}
        self._rgb_to_color = {}
    @classmethod
    def hex_to_rgb(cls, hex_color):
        hex_color = hex_color.lstrip('#')
        if len(hex_color) != 6:
            raise ValueError("Invalid hexadecimal color format")
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        return (r, g, b)
    def add_color(self, hex_code, name):
        rgb = self.hex_to_rgb(hex_code)
        if rgb in self._rgb_to_color:
            return
        self._color_to_rgb[name] = rgb
        self._rgb_to_color[rgb] = name
    def get_color_name_from_rgb(self, r, g, b):
        rgb = (r, g, b)
        return self._rgb_to_color.get(rgb, "Unknown Color")
    def get_rgb_from_name(self, name):
        rgb = self._color_to_rgb.get(name)
        if rgb is None:
            raise KeyError(f"Color '{name}' not found")
        return rgb
if __name__ == '__main__':
    manager = ColorManager()
    manager.add_color("#FF0000", "Red")
    manager.add_color("#00FF00", "Green")
    manager.add_color("#0000FF", "Blue")
    manager.add_color("#FFFFFF", "White")
    manager.add_color("#000000", "Black")
    print(f"Color name for RGB (255, 0, 0): {manager.get_color_name_from_rgb(255, 0, 0)}")
    print(f"Color name for RGB (0, 128, 0): {manager.get_color_name_from_rgb(0, 128, 0)}")
    print(f"Color name for RGB (10, 20, 30): {manager.get_color_name_from_rgb(10, 20, 30)}")
    print(f"Color name for RGB (255, 255, 255): {manager.get_color_name_from_rgb(255, 255, 255)}")
    try:
        print(f"RGB for 'Red': {manager.get_rgb_from_name('Red')}")
        print(f"RGB for 'Blue': {manager.get_rgb_from_name('Blue')}")
        print(f"Color name for unknown RGB (1, 1, 1): {manager.get_color_name_from_rgb(1, 1, 1)}")
    except KeyError as e:
        print(e)