class ColorManager:
    def __init__(self):
        self._color_to_rgb = {}
        self._rgb_to_color = {}
    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip('#')
        if len(hex_color) != 6:
            raise ValueError("Invalid hex color format")
        try:
            r = int(hex_color[0:2], 16)
            g = int(hex_color[2:4], 16)
            b = int(hex_color[4:6], 16)
            return r, g, b
        except ValueError:
            raise ValueError("Invalid hexadecimal characters in color")
    def add_color(self, hex_color, name):
        r, g, b = self.hex_to_rgb(hex_color)
        rgb_tuple = (r, g, b)
        self._color_to_rgb[name] = rgb_tuple
        self._rgb_to_color[rgb_tuple] = name
    def get_color_name_from_rgb(self, r, g, b):
        rgb_tuple = (r, g, b)
        return self._rgb_to_color.get(rgb_tuple, "Unknown Color")
if __name__ == '__main__':
    manager = ColorManager()
    sample_colors = [
        ("#FF0000", "Red"),
        ("#00FF00", "Green"),
        ("#0000FF", "Blue"),
        ("#FFFFFF", "White"),
        ("#000000", "Black")
    ]
    for hex_code, name in sample_colors:
        manager.add_color(hex_code, name)
    print("--- Retrieving color names by RGB ---")
    test_rgb_1 = (255, 0, 0)
    print(f"RGB ({test_rgb_1[0]}, {test_rgb_1[1]}, {test_rgb_1[2]}): {manager.get_color_name_from_rgb(*test_rgb_1)}")
    test_rgb_2 = (0, 255, 0)
    print(f"RGB ({test_rgb_2[0]}, {test_rgb_2[1]}, {test_rgb_2[2]}): {manager.get_color_name_from_rgb(*test_rgb_2)}")
    test_rgb_3 = (0, 0, 255)
    print(f"RGB ({test_rgb_3[0]}, {test_rgb_3[1]}, {test_rgb_3[2]}): {manager.get_color_name_from_rgb(*test_rgb_3)}")
    test_rgb_4 = (255, 255, 255)
    print(f"RGB ({test_rgb_4[0]}, {test_rgb_4[1]}, {test_rgb_4[2]}): {manager.get_color_name_from_rgb(*test_rgb_4)}")
    test_rgb_5 = (10, 20, 30)
    print(f"RGB ({test_rgb_5[0]}, {test_rgb_5[1]}, {test_rgb_5[2]}): {manager.get_color_name_from_rgb(*test_rgb_5)}")
    test_rgb_6 = (128, 128, 128)
    print(f"RGB ({test_rgb_6[0]}, {test_rgb_6[1]}, {test_rgb_6[2]}): {manager.get_color_name_from_rgb(*test_rgb_6)}")