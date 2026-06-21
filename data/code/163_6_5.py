from typing import List, Tuple

def validate_pairs(pairs: List[Tuple[str, str]]) -> bool:
    schema = {
        "apple": "red",
        "banana": "yellow",
        "grape": "purple",
        "orange": "orange"
    }
    return all(pair in schema.items() for pair in pairs)

if __name__ == '__main__':
    sample_pairs = [
        ("apple", "red"),
        ("banana", "yellow"),
        ("grape", "purple"),
        ("orange", "orange")
    ]
    print(validate_pairs(sample_pairs))