import json

def generate_fruit_color_json():
    fruit_colors = [
        {"fruit": "apple", "color": "red"},
        {"fruit": "banana", "color": "yellow"},
        {"fruit": "grape", "color": "purple"}
    ]
    return json.dumps(fruit_colors, separators=(',', ':'))

if __name__ == '__main__':
    sample_json = generate_fruit_color_json()
    print(sample_json)