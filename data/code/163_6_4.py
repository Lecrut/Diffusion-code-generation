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

if __name__ == '__main__':
    sample_pairs = [
        ("Apple", "Red"),
        ("Banana", "Yellow"),
        ("Grape", "Purple"),
        ("Orange", "Orange"),
        ("Strawberry", "Red"),
        ("Pineapple", "Yellow")
    ]
    
    print(validate_pairs(sample_pairs))