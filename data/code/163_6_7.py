from typing import List, Tuple

def validate_pairs(fruit_color_pairs: List[Tuple[str, str]]) -> bool:
    schema = {
        "Apple": "Red",
        "Banana": "Yellow",
        "Grape": "Purple",
        "Orange": "Orange",
        "Strawberry": "Red",
        "Pineapple": "Yellow"
    }
    for fruit, color in fruit_color_pairs:
        if fruit not in schema or schema[fruit] != color:
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