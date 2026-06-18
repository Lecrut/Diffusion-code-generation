import re
from typing import List, Dict
def sanitize_input(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    sanitized = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return sanitized.strip()
def get_animal_preferences(preferences: List[str]) -> Dict[str, int]:
    if not isinstance(preferences, list):
        raise TypeError("Preferences must be provided as a list.")
    cleaned_preferences = []
    for item in preferences:
        if not isinstance(item, str):
            continue                                                  
        sanitized_item = sanitize_input(item)
        if sanitized_item and sanitized_item[0].isalpha():
            cleaned_preferences.append(sanitized_item.lower())
    preference_counts: Dict[str, int] = {}
    for pref in cleaned_preferences:
        if pref not in preference_counts:
            preference_counts[pref] = 0
        preference_counts[pref] += 1
    return preference_counts
if __name__ == '__main__':
    raw_preferences = [
        "dog", 
        "cat# $%", 
        "\"injection\"; rm -rf /", 
        "bird\t\n", 
        "", 
        "fish" * 3, 
        "reptile!"
    ]
    final_counts = get_animal_preferences(raw_preferences)
    print("Animal Preference Tracking Results:")
    for animal, count in sorted(final_counts.items()):
        print(f"{animal}: {count}")