import re
from typing import Dict, List
class AnimalPreferenceTracker:
    def __init__(self):
        self.preferences: Dict[str, str] = {}
    @staticmethod
    def sanitize_input(text: str) -> str:
        allowed_pattern = r'^[a-zA-Z0-9\s\-\']+$'
        return re.sub(r'[^\w\s\-\'"]', '', text).strip()
    def add_preference(self, animal: str, food_type: str) -> None:
        sanitized_animal = self.sanitize_input(animal)
        sanitized_food = self.sanitize_input(food_type)
        if not sanitized_animal or not sanitized_food:
            raise ValueError("Animal and food type cannot be empty.")
        self.preferences[sanitized_animal] = sanitized_food
    def get_preferences(self, animal: str) -> List[str]:
        return self.preferences.get(self.sanitize_input(animal), [])
if __name__ == '__main__':
    tracker = AnimalPreferenceTracker()
    sample_data = [
        ("lion", "meat"),
        ("elephant", "grass"),
        ("tiger", "fish")
    ]
    for animal, food in sample_data:
        try:
            tracker.add_preference(animal, food)
            print(f"Added preference for {animal}: {food}")
        except ValueError as e:
            print(f"Error adding preference: {e}")
    test_input = "  user@input#123% "
    cleaned = AnimalPreferenceTracker.sanitize_input(test_input)
    print(f"Sanitized input '{test_input}' -> '{cleaned}'")