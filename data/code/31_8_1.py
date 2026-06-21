COLOR_HEX_MAP = {
    "#FF0000": (255, 0, 0),
    "#00FF00": (0, 255, 0),
    "#0000FF": (0, 0, 255),
    "#FFFFFF": (255, 255, 255),
    "#000000": (0, 0, 0),
    "#FFFF00": (255, 255, 0),
    "#FF00FF": (255, 0, 255),
    "#00FFFF": (0, 255, 255)
}

def get_decimal_color(hex_code: str) -> tuple:
    cleaned = hex_code.lstrip("#").upper()
    if cleaned in [k.lstrip("#").upper() for k in COLOR_HEX_MAP.keys()]:
        for k, v in COLOR_HEX_MAP.items():
            if k.lstrip("#").upper() == cleaned:
                return v
    red = int(cleaned[0:2], 16)
    green = int(cleaned[2:4], 16)
    blue = int(cleaned[4:6], 16)
    return (red, green, blue)

if __name__ == '__main__':
    print(get_decimal_color("#FF0000"))
    print(get_decimal_color("#1A2B3C"))