class ColorMapper:
    def __init__(self):
        self.hex_to_name = {
            "#FF0000": "Red",
            "#00FF00": "Green",
            "#0000FF": "Blue",
            "#FFFF00": "Yellow",
            "#FFA500": "Orange",
            "#800080": "Purple",
            "#00FFFF": "Cyan",
            "#FFFFFF": "White",
            "#000000": "Black"
        }
    def map_hex_to_name(self, hex_color: str) -> str:
        if not isinstance(hex_color, str):
            return "Invalid Input Type"
        hex_color = hex_color.strip()
        if len(hex_color) != 7 or not hex_color.startswith('#'):
            return "Invalid Hex Format"
        if hex_color in self.hex_to_name:
            return self.hex_to_name[hex_color]
        else:
            return "Color Not Found"
if __name__ == '__main__':
    mapper = ColorMapper()
    colors_to_test = [
        "#FF0000",
        "#00FF00",
        "#0000FF",
        "#FFFFFF",
        "#000000",
        "#123456"
    ]
    for color in colors_to_test:
        result = mapper.map_hex_to_name(color)
        print(f"Hex: {color}, Name: {result}")