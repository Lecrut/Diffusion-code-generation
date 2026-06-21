import json

def generate_fruit_color_json():
    fruit_colors = [
        ("Apple", "Red"),
        ("Banana", "Yellow"),
        ("Cherry", "Red"),
        ("Date", "Brown"),
        ("Elderberry", "Purple")
    ]
    return json.dumps(fruit_colors, separators=(',', ':'))

if __name__ == '__main__':
    print(generate_fruit_color_json())