from typing import List
class AnimalTracker:
    def __init__(self) -> None:
        self.animal_names: List[str] = []
    def add_animal(self, name: str) -> bool:
        if not isinstance(name, str):
            return False
        for existing in self.animal_names:
            if existing == name:
                return False
        self.animal_names.append(name)
        return True
    def remove_animal(self, name: str) -> bool:
        try:
            index = self.animal_names.index(name)
            del self.animal_names[index]
            return True
        except ValueError:
            return False
    def get_all_animals(self) -> List[str]:
        return list(self.animal_names)
def run_tests() -> None:
    tracker = AnimalTracker()
    assert not tracker.add_animal("Lion") or "Lion" in tracker.get_all_animals(), "Add Lion failed"
    assert len(tracker.get_all_animals()) == 1, "Count mismatch after adding one animal"
    assert tracker.remove_animal("Lion"), "Remove Lion failed"
    assert len(tracker.get_all_animals()) == 0, "Empty list check failed"
if __name__ == '__main__':
    run_tests()