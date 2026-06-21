from typing import List, Tuple

def validate_fruit_color_pair(fruit: str, color: str) -> bool:
    schema = {
        "Apple": "Red",
        "Banana": "Yellow",
        "Grape": "Purple",
        "Orange": "Orange",
        "Strawberry": "Red",
        "Pineapple": "Yellow"
    }
    return schema.get(fruit, None) == color

def validate_pairs(pairs: List[Tuple[str, str]]) -> bool:
    for fruit, color in pairs:
        if not validate_fruit_color_pair(fruit, color):
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