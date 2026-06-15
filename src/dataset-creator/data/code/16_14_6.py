class ColorManager:
    def __init__(self):
        self._color_to_rgb = {}
        self._rgb_to_color = {}
    @classmethod
    def hex_to_rgb(cls, hex_color):
        if not hex_color.startswith('#'):
            raise ValueError("Invalid hex color format")
        hex_value = hex_color[1:]
        if len(hex_value) != 6:
            raise ValueError("Hex color must be 6 digits long")
        try:
            r = int(hex_value[0:2], 16)
            g = int(hex_value[2:4], 16)
            b = int(hex_value[4:6], 16)
            rgb = (r, g, b)
            return rgb
        except ValueError:
            raise ValueError("Invalid hexadecimal characters in color string")
    def add_color(self, hex_color, name):
        rgb = self.hex_to_rgb(hex_color)
        if rgb not in self._color_to_rgb:
            self._color_to_rgb[rgb] = name
            self._rgb_to_color[rgb] = name
    def get_color_name_from_rgb(self, r, g, b):
        rgb = (r, g, b)
        return self._rgb_to_color.get(rgb, "Unknown Color")
if __name__ == '__main__':
    manager = ColorManager()
    sample_colors = [
        ("#FF0000", "Red"),
        ("#00FF00", "Green"),
        ("#0000FF", "Blue"),
        ("#FFFFFF", "White"),
        ("#000000", "Black")
    ]
    for hex_color, name in sample_colors:
        manager.add_color(hex_color, name)
    print("--- Stored Colors (Hex to Name) ---")
    for hex_color, name in sample_colors:
        rgb = ColorManager.hex_to_rgb(hex_color)
        print(f"Hex: {hex_color}, Name: {name}, RGB: {rgb}")
    print("\n--- Retrieval by RGB (RGB to Hex) ---")
    test_rgb_1 = (255, 0, 0)
    print(f"RGB ({test_rgb_1[0]}, {test_rgb_1[1]}, {test_rgb_1[2]}) maps to: {manager.get_color_name_from_rgb(*test_rgb_1)}")
    test_rgb_2 = (0, 255, 0)
    print(f"RGB ({test_rgb_2[0]}, {test_rgb_2[1]}, {test_rgb_2[2]}) maps to: {manager.get_color_name_from_rgb(*test_rgb_2)}")
    test_rgb_3 = (10, 20, 30)
    print(f"RGB ({test_rgb_3[0]}, {test_rgb_3[1]}, {test_rgb_3[2]}) maps to: {manager.get_color_name_from_rgb(*test_rgb_3)}")
    test_rgb_4 = (255, 255, 255)
    print(f"RGB ({test_rgb_4[0]}, {test_rgb_4[1]}, {test_rgb_4[2]}) maps to: {manager.get_color_name_from_rgb(*test_rgb_4)}")
    test_rgb_5 = (128, 128, 128)
    print(f"RGB ({test_rgb_5[0]}, {test_rgb_5[1]}, {test_rgb_5[2]}) maps to: {manager.get_color_name_from_rgb(*test_rgb_5)}")