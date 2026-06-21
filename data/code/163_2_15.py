import json

def generate_fruit_color_json():
    fruit_colors = [
        ("apple", "red"),
        ("banana", "yellow"),
        ("grape", "purple"),
        ("orange", "orange"),
        ("strawberry", "red")
    ]
    return json.dumps(fruit_colors, separators=(',', ':'))

if __name__ == '__main__':
    print(generate_fruit_color_json())