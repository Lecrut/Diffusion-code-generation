from typing import List, Tuple

class FruitColorValidator:
    def __init__(self):
        self.schema = {
            "apple": "red",
            "banana": "yellow",
            "grape": "purple",
            "orange": "orange",
            "strawberry": "red",
            "pineapple": "yellow"
        }

    def validate_pairs(self, pairs: List[Tuple[str, str]]) -> bool:
        for fruit, color in pairs:
            if fruit.lower() not in self.schema or self.schema[fruit.lower()] != color.lower():
                return False
        return True

if __name__ == '__main__':
    validator = FruitColorValidator()
    sample_pairs = [
        ("Apple", "Red"),
        ("Banana", "Yellow"),
        ("Grape", "Purple"),
        ("Orange", "Orange"),
        ("Strawberry", "Red"),
        ("Pineapple", "Yellow")
    ]
    print(validator.validate_pairs(sample_pairs))