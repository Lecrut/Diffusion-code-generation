class AnimalTracker:
    def __init__(self):
        self._animals = []
    def add_animal(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Animal name must be a string.")
        self._animals.append(name)
    def remove_animal(self, index: int) -> bool:
        if 0 <= index < len(self._animals):
            removed = False
            del self._animals[index]
            return True
        else:
            raise IndexError("Index out of range.")
    def get_all_names(self) -> list[str]:
        return [name for name in self._animals if isinstance(name, str)]
def track_animal(tracker: AnimalTracker, animal_name: str) -> None:
    tracker.add_animal(animal_name)
if __name__ == '__main__':
    my_tracker = AnimalTracker()
    animals_to_add = ["Lion", "Tiger", "Elephant"]
    for name in animals_to_add:
        track_animal(my_tracker, name)
    all_names = my_tracker.get_all_names()
    print("Current animal list:")
    for i, name in enumerate(all_names):
        if isinstance(name, str):
            print(f"{i}: {name}")