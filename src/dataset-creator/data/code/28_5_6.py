import re
from typing import Dict, List
def sanitize_input(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    sanitized = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return sanitized.strip()
def get_animal_preferences(animals: List[str], preferences: Dict[str, str]) -> Dict[str, int]:
    cleaned_animals = [sanitize_input(animal) for animal in animals]
    final_counts: Dict[str, int] = {animal: 0 for animal in cleaned_animals}
    for user_choice in preferences.values():
        sanitized_choice = sanitize_input(user_choice)
        if sanitized_choice in final_counts:
            final_counts[sanitized_choice] += 1
    return final_counts
if __name__ == '__main__':
    sample_animals = ["Lion", "Tiger", "Elephant"]
    raw_preferences_input: Dict[str, str] = {
        "user1": "  Tiger   ", 
        "user2": "<script>alert('xss')</script> Elephant",
        "user3": "\"SELECT * FROM animals WHERE name='Lion'",
        "user4": "Normal choice"
    }
    raw_choices = [val for val in raw_preferences_input.values() if 'Tiger' in val or 'Elephant' in val or 'Lion' in val]
    result: Dict[str, int] = get_animal_preferences(sample_animals, {"user1": "Tiger", "user2": "Elephant"})
    print("Sanitized Preferences:")
    for animal, count in sorted(result.items()):
        if count > 0:
            print(f"{animal}: {count}")