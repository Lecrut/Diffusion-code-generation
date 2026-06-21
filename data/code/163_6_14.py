from typing import List, Tuple

def validate_pairs(pairs: List[Tuple[str, str]]) -> bool:
    schema = {
        "apple": "red",
        "banana": "yellow",
        "cherry": "red"
    }
    
    for fruit, color in pairs:
        if fruit not in schema or schema[fruit] != color:
            return False
    return True

if __name__ == '__main__':
    sample_pairs = [
        ("apple", "red"),
        ("banana", "yellow"),
        ("cherry", "red")
    ]
    
    print(validate_pairs(sample_pairs))