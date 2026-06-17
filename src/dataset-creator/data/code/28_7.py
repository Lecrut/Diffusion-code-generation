import unittest
class AnimalTracker:
    def __init__(self):
        self._animals = []
    def add_animal(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Animal name must be a string")
        self._animals.append(name)
    def get_all_names(self) -> list[str]:
        return list(self._animals)
class TestAnimalTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = AnimalTracker()
    def test_add_animal_appends_to_list(self):
        self.tracker.add_animal("Lion")
        expected = ["Lion"]
        actual = self.tracker.get_all_names()
        self.assertEqual(actual, expected)
    def test_multiple_animals_added(self):
        self.tracker.add_animal("Tiger")
        self.tracker.add_animal("Elephant")
        expected = ["Tiger", "Elephant"]
        actual = self.tracker.get_all_names()
        self.assertEqual(actual, expected)
    def test_invalid_name_raises_error(self):
        with self.assertRaises(TypeError):
            self.tracker.add_animal(123)
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False, verbosity=0)