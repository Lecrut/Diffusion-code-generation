import unittest
class AnimalTracker:
    def __init__(self):
        self._animals = []
    def add_animal(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Animal name must be a string")
        self._animals.append(name)
    def get_animals(self) -> list[str]:
        return list(self._animals)
    def remove_animal(self, name: str) -> bool:
        try:
            index = self._animals.index(name)
            del self._animals[index]
            return True
        except ValueError:
            return False
class TestAnimalTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = AnimalTracker()
    def test_add_animal(self):
        self.tracker.add_animal("Lion")
        result = self.tracker.get_animals()
        self.assertEqual(result, ["Lion"])
    def test_remove_nonexistent_animal(self):
        initial_count = len(self.tracker._animals)
        removed = self.tracker.remove_animal("Tiger")
        self.assertFalse(removed)
        self.assertEqual(len(self.tracker._animals), initial_count)
    def test_add_and_remove_same_animal(self):
        self.tracker.add_animal("Elephant")
        result_before = len(self.tracker.get_animals())
        removed = self.tracker.remove_animal("Elephant")
        self.assertTrue(removed)
        result_after = len(self.tracker._animals)
        self.assertEqual(result_before - 1, result_after)
if __name__ == '__main__':
    unittest.main()