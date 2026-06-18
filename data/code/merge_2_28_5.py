import re
from typing import Dict, List
class AnimalPreferenceTracker:
    def __init__(self):
        self.preferences: Dict[str, List[str]] = {}
    def sanitize_input(self, text: str) -> str:
        safe_text = re.sub(r"(?i)(union|select|insert|delete|drop|execute)", "", text, flags=re.IGNORECASE)
        safe_text = re.sub(r"[^\w\s]", "", safe_text)
        return " ".join(safe_text.split())
    def add_preference(self, animal: str, food_type: str) -> None:
        sanitized_animal = self.sanitize_input(animal)
        sanitized_food = self.sanitize_input(food_type)
        if not sanitized_animal or not sanitized_food:
            raise ValueError("Animal and food type cannot be empty.")
        animal_lower = sanitized_animal.lower()
        if animal_lower in self.preferences:
            if sanitized_food not in self.preferences[animal_lower]:
                self.preferences[animal_lower].append(sanitized_food)
        else:
            self.preferences[animal_lower] = [sanitized_food]
    def get_preferences(self, animal: str) -> List[str]:
        sanitized_animal = self.sanitize_input(animal)
        return sorted(self.preferences.get(sanitized_animal.lower(), []))
if __name__ == '__main__':
    tracker = AnimalPreferenceTracker()
    animals_data = [
        ("lion", "meat"),
        ("elephant", "grass"),
        ("monkey", "fruit"),
        ("dog", "bone"),
        ("cat", "fish")
    ]
    injection_attempts = ["' OR '1'='1'", "<script>alert('xss')</script>", "; DROP TABLE users;"]
    for animal, food in animals_data:
        tracker.add_preference(animal, food)
    print("Animal Preferences Recorded:")
    for animal, foods in sorted(tracker.preferences.items()):
        print(f"{animal}: {foods}")
    try:
        bad_input = "zebra; DROP TABLE preferences"
        tracker.add_preference(bad_input.split(";")[0], "leaves")                                                                                                      
        print("\nSanitized Input Test:")
        result = tracker.get_preferences("zebra")
        if result:
            print(f"Cleaned preference found for 'zebra': {result}")
        else:
            clean_zebra_input = "zebra leaves".split()
            tracker.add_preference(clean_zebra_input[0], clean_zebra_input[1])
            print(f"Final preference for 'zebra': {tracker.get_preferences('zebra')}")
    except ValueError as e:
        print(f"Error occurred: {e}")