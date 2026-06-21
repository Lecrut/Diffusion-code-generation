from typing import List, Tuple

def validate_schema(fruit_color_pairs: List[Tuple[str, str]]) -> bool:
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

def display_fruit_color_pairs(fruit_color_pairs: List[Tuple[str, str]]) -> None:
    if not validate_schema(fruit_color_pairs):
        print("Validation failed.")
        return
    max_fruit_len = max(len(fruit) for fruit, _ in fruit_color_pairs)
    max_color_len = max(len(color) for _, color in fruit_color_pairs)
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