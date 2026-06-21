import json

def generate_fruit_color_json():
    fruits = [
        ("apple", "red"),
        ("banana", "yellow"),
        ("cherry", "red"),
        ("date", "brown")
    ]
    
    fruit_color_dict = {fruit: color for fruit, color in fruits}
    return json.dumps(fruit_color_dict, separators=(',', ':'))

if __name__ == '__main__':
    print(generate_fruit_color_json())