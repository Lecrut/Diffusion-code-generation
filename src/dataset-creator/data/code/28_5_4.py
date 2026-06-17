import re
from typing import List, Dict
class AnimalPreferenceTracker:
    def __init__(self):
        self.preferences: Dict[str, List[str]] = {}
    def sanitize_input(self, data: str) -> str:
        sanitized = re.sub(r'[^\w\s.,!?-]', '', data)
        return sanitized.strip()
    def add_preference(self, animal_name: str, food_item: str) -> None:
        if not re.match(r'^[A-Za-z0-9_]+$', animal_name):
            raise ValueError("Animal names must contain only alphanumeric characters and underscores.")
        safe_food = self.sanitize_input(food_item)
        if not safe_food:
            raise ValueError("Food item cannot be empty after sanitization.")
        animal_name_lower = animal_name.lower()
        if animal_name_lower not in self.preferences:
            self.preferences[animal_name_lower] = []
        if safe_food.lower() not in [item.lower() for item in self.preferences[animal_name_lower]]:
            self.preferences[animal_name_lower].append(safe_food)
if __name__ == '__main__':
    tracker = AnimalPreferenceTracker()
    test_cases = [
        ("Lion", "Meatballs"),
        ("Tiger", "<script>alert('xss')</script> Meat"),                                
        ("Elephant", "Bananas & Apples!@#$%"),                                           
        ("Cat_", "_underscore_test_ Food")                                              
    ]
    for animal, food in test_cases:
        try:
            tracker.add_preference(animal, food)
            print(f"Added preference for {animal}: {food}")
        except ValueError as e:
            print(f"Validation Error for {animal} and '{food[:20]}...': {e}")
    print("\nFinal Preferences:")
    for animal, items in tracker.preferences.items():
        display_items = ", ".join(items)
        print(f"{animal.capitalize()}: [{display_items}]")