import re
class FavoriteAnimalStore:
    def __init__(self):
        self._lookup = {}                                                    
    def add(self, animal_name: str) -> None:
        normalized_key = animal_name.lower().strip()
        if not re.match(r'^[a-zA-Z]+$', normalized_key):
            raise ValueError("Animal names must contain only alphabetic characters.")
        self._lookup[normalized_key] = True
    def has(self, search_term: str) -> bool:
        return re.match(r'^[a-zA-Z]+$', search_term.lower().strip()) and\
               search_term.lower().strip() in self._lookup
if __name__ == '__main__':
    store = FavoriteAnimalStore()
    animals_to_add = ["Lion", "Tiger", "Elephant"]
    for animal in animals_to_add:
        try:
            store.add(animal)
        except ValueError as e:
            print(f"Error adding {animal}: {e}")
    test_cases = [
        "lion",                         
        "LION",                         
        "  Lion  ",                    
        "cat",                                    
        "123abc"                         
    ]
    for test_case in test_cases:
        result = store.has(test_case)
        print(f"'{test_case}' exists: {result}")