import json

def generate_fruit_color_json():
    fruit_colors = [
        {"fruit": "apple", "color": "red"},
        {"fruit": "banana", "color": "yellow"}
    ]
    return json.dumps(fruit_colors, separators=(',', ':'))

if __name__ == '__main__':
    print(generate_fruit_color_json())