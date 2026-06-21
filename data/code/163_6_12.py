from typing import List, Tuple

def validate_pairs(pairs: List[Tuple[str, str]]) -> bool:
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

def display_validation_result(pairs: List[Tuple[str, str]]) -> None:
    is_valid = validate_pairs(pairs)
    print(f"Validation Result: {'Valid' if is_valid else 'Invalid'}")

if __name__ == '__main__':
    sample_data = [
        ("Apple", "Red"),
        ("Banana", "Yellow"),
        ("Grape", "Purple"),
        ("Orange", "Orange"),
        ("Strawberry", "Red"),
        ("Pineapple", "Yellow")
    ]
    display_validation_result(sample_data)