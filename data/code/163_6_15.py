from typing import List, Tuple

def validate_schema(pairs: List[Tuple[str, str]]) -> bool:
    schema = {
        "apple": "red",
        "banana": "yellow",
        "grape": "purple",
        "orange": "orange",
        "strawberry": "red",
        "pineapple": "yellow"
    }
    for fruit, color in pairs:
        if fruit.lower() not in schema or schema[fruit.lower()] != color.lower():
            return False
    return True

def display_fruit_color_pairs(fruit_color_pairs: List[Tuple[str, str]]) -> None:
    if not validate_schema(fruit_color_pairs):
        raise ValueError("Invalid fruit-color pairs")
    max_fruit_len = max(len(fruit) for fruit, color in fruit_color_pairs)
    max_color_len = max(len(color) for fruit, color in fruit_color_pairs)
    for fruit, color in fruit_color_pairs:
        print(f"{fruit:<{max_fruit_len}} | {color:<{max_color_len}}")

if __name__ == '__main__':
    sample_data = [
        ("Apple", "Red"),
        ("Banana", "Yellow"),
        ("Grape", "Purple"),
        ("Orange", "Orange"),
        ("Strawberry", "Red"),
        ("Pineapple", "Yellow")
    ]
    display_fruit_color_pairs(sample_data)