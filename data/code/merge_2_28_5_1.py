import re
from typing import Dict, List
def sanitize_input(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    sanitized = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return sanitized.strip()
def track_animal_preferences(animals: List[str], preferences: Dict[str, str]) -> Dict[str, int]:
    sanitized_animals = [sanitize_input(animal) for animal in animals]
    sanitized_preferences = {key: sanitize_input(value) for key, value in preferences.items()}
    counts: Dict[str, int] = {}
    for animal in sanitized_animals:
        if animal not in sanitized_preferences:
            continue
        preference_item = sanitized_preferences[animal]
        counts[preference_item] = counts.get(preference_item, 0) + 1
    return counts
if __name__ == '__main__':
    sample_animals = ["Lion", "Tiger", "Bear"]
    raw_preferences_input: Dict[str, str] = {
        "Lion": "meat",
        "Tiger": "fish",
        "Bear": "honey"
    }
    test_injection_data: List[str] = ["' OR 1=1 -- ", '" AND "admin"', "<script>alert('xss')</script>"]
    final_animals = sample_animals + [animal for animal in test_injection_data if not re.match(r'^[a-zA-Z]+$', animal)]
    raw_prefs_input: Dict[str, str] = {
        "Lion": "' DROP TABLE users; --",
        "Tiger": "<img src=x onerror=alert(1)>",
        "Bear": '" OR 1=1'
    }
    result_preferences = track_animal_preferences(final_animals, raw_prefs_input)
    print("Sanitized Animal Preferences:")
    for animal in final_animals:
        if animal not in test_injection_data and sanitize_input(animal) != "":
            preference_item = sanitize_input(raw_prefs_input.get(sanitize_input(animal), ""))
            count = result_preferences.get(preference_item, 0)
            print(f"{animal}: {preference_item} (Count: {count})")
    for animal in test_injection_data:
        cleaned_animal = sanitize_input(animal)
        if cleaned_animal and not re.match(r'^[a-zA-Z]+$', cleaned_animal):
            print(f"Injected string '{animal}' was correctly filtered/sanitized to '{cleaned_animal}'.")
    all_items = list(result_preferences.keys()) + [sanitize_input(animal) for animal in sample_animals]
    has_special_chars = any(re.search(r'[^\w\s]', item) for item in all_items if isinstance(item, str))
    print(f"Final preference items contain special characters: {has_special_chars}")