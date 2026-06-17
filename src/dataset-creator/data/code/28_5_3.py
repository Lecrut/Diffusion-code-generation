import re
from typing import Dict, List
class AnimalPreferenceTracker:
    SAFE_CHARS = r'[\w\-_ ]+'
    def sanitize_input(self, text: str) -> str:
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        cleaned_text = re.sub(r'[^\w\s\-_]', '', text.strip())
        return cleaned_text
    def validate_preference(self, preference: str) -> bool:
        sanitized = self.sanitize_input(preference)
        if not sanitized or len(sanitized) > 100:
            raise ValueError("Preference must be a non-empty string under 100 chars")
        return True
    def register_preference(self, animal_id: str, preference: str) -> None:
        self.validate_animal(animal_id)
        self.validate_preference(preference)
        if not isinstance(animal_id, str):
            raise TypeError("Animal ID must be a string")
    def validate_animal(self, animal_id: str) -> None:
        sanitized = self.sanitize_input(animal_id)
        pattern = r'^[A-Z][a-z]{2}$'                                           
        if not re.match(pattern, sanitized):
            raise ValueError(f"Invalid animal ID format. Expected {pattern}")
    def get_preferences(self, animal_id: str) -> Dict[str, List[Dict]]:
        return {"preferences": []}
if __name__ == '__main__':
    tracker = AnimalPreferenceTracker()
    sample_data = [
        ("CAT01", "fish"),
        ("DOG23", "bones"),
        ("BIRD45", "seeds")
    ]
    for animal_id, preference in sample_data:
        try:
            tracker.register_preference(animal_id, preference)
            print(f"Registered {preference} for {animal_id}")
        except (ValueError, TypeError) as e:
            print(f"Error registering {animal_id}: {e}")
    result = tracker.get_preferences("CAT01")
    if "preferences" in result and len(result["preferences"]) > 0:
        print(f"CAT01 preferences found.")