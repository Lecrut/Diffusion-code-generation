from typing import List, Tuple

def is_valid_fruit_color(fruit: str, color: str) -> bool:
    schema = {
        "apple": "red",
        "banana": "yellow",
        "grape": "purple",
        "orange": "orange",
        "strawberry": "red",
        "pineapple": "yellow"
    }
    return fruit in schema and schema[fruit] == color

def validate_pairs(fruit_color_pairs: List[Tuple[str, str]]) -> bool:
    for fruit, color in fruit_color_pairs:
        if not is_valid_fruit_color(fruit.lower(), color.lower()):
            return False
    return True

if __name__ == '__main__':
    sample_data = [
        ("Apple", "Red"),
        ("Banana", "Yellow"),
        ("Grape", "Purple"),
        ("Orange", "Orange"),
        ("Strawberry", "Red"),
        ("Pineapple", "Yellow")
    ]
    print(validate_pairs(sample_data))