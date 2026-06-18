import unittest
class AnimalTracker:
    def __init__(self):
        self.animals = []
    def add_animal(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Animal name must be a string")
        self.animals.append(name)
    def remove_animal(self, index: int) -> bool:
        try:
            removed = self.animals.pop(index)
            return True
        except IndexError:
            return False
    def get_all_names(self) -> list[str]:
        return list(self.animals)
class TestAnimalTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = AnimalTracker()
    def test_add_animal_success(self):
        result = self.tracker.add_animal("Lion")
        self.assertTrue(result is None)
        names = self.tracker.get_all_names()
        self.assertEqual(names, ["Lion"])
    def test_remove_first_animal(self):
        self.tracker.add_animal("Tiger")
        removed = self.tracker.remove_animal(0)
        self.assertTrue(removed)
        names = self.tracker.get_all_names()
        self.assertNotIn("Tiger", names)
    def test_add_invalid_type_raises_error(self):
        with self.assertRaises(TypeError):
            self.tracker.add_animal(123)
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False, verbosity=2)