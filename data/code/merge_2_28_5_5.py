import re
from typing import Dict, List
def sanitize_input(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    sanitized = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return sanitized.strip()
def get_animal_preferences(data: Dict[str, List[str]]) -> Dict[str, int]:
    preferences: Dict[str, int] = {}
    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary.")
    for key in data.keys():
        if not sanitize_input(key).isalpha() or len(sanitize_input(key)) == 0:
            continue
        animal_name = sanitize_input(key)
        count = sum(1 for item in data[key] if isinstance(item, str) and re.match(r'^[a-zA-Z]+$', item.strip()))
        preferences[animal_name] = max(count, 0)
    return preferences
if __name__ == '__main__':
    sample_data: Dict[str, List[str]] = {
        "dogs": ["cat", "dog", "fish"],
        "cats": ["bird", "mouse", "insect"],
        "birds": ["seed", "water"]
    }
    cleaned_preferences = get_animal_preferences(sample_data)
    for animal, count in sorted(cleaned_preferences.items(), key=lambda x: -x[1]):
        print(f"{animal}: {count}")