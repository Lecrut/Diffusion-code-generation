import json

FRUIT_COLOR_DATA = [
    {"fruit": "Apple", "color": "Red"},
    {"fruit": "Banana", "color": "Yellow"},
    {"fruit": "Grape", "color": "Purple"}
]

def generate_fruit_color_json(data):
    return json.dumps(data, separators=(',', ':'))

if __name__ == '__main__':
    print(generate_fruit_color_json(FRUIT_COLOR_DATA))