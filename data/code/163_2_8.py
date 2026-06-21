import json

def generate_fruit_color_json():
    fruit_colors = [
        ("apple", "red"),
        ("banana", "yellow"),
        ("cherry", "red"),
        ("date", "brown"),
        ("elderberry", "purple")
    ]
    return json.dumps({fruit: color for fruit, color in fruit_colors}, separators=(',', ':'))

if __name__ == '__main__':
    print(generate_fruit_color_json())