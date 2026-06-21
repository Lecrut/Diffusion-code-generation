import json

FRUIT_COLOR_MAP = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple"
}

def generate_fruit_color_json():
    fruit_colors = [{"fruit": fruit, "color": color} for fruit, color in FRUIT_COLOR_MAP.items()]
    return json.dumps(fruit_colors, separators=(',', ':'))

if __name__ == '__main__':
    print(generate_fruit_color_json())