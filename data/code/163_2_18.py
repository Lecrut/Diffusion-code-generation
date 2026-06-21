import json

def validate_fruit_color_pairs(pairs):
    if not all(isinstance(pair, tuple) and len(pair) == 2 for pair in pairs):
        raise ValueError("Invalid fruit-color pairs. Each item must be a tuple of two elements.")
    return pairs

def generate_fruit_color_json(pairs):
    validated_pairs = validate_fruit_color_pairs(pairs)
    fruit_colors = [{"fruit": pair[0], "color": pair[1]} for pair in validated_pairs]
    return json.dumps(fruit_colors, separators=(',', ':'))

if __name__ == '__main__':
    pairs = [("Apple", "Red"), ("Banana", "Yellow"), ("Grape", "Purple")]
    print(generate_fruit_color_json(pairs))