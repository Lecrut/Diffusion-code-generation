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
            del self.animals[index]
            return True
        except IndexError:
            return False
    def get_all_names(self) -> list:
        return self.animals.copy()
class TestAnimalTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = AnimalTracker()
    def test_add_animal_success(self):
        self.tracker.add_animal("Lion")
        expected = ["Lion"]
        actual = self.tracker.get_all_names()
        self.assertEqual(actual, expected)
    def test_remove_first_animal(self):
        self.tracker.add_animal("Tiger")
        result = self.tracker.remove_animal(0)
        self.assertTrue(result)
        expected = []
        actual = self.tracker.get_all_names()
        self.assertEqual(actual, expected)
    def test_remove_nonexistent_index(self):
        result = self.tracker.remove_animal(-1)
        self.assertFalse(result)
if __name__ == '__main__':
    unittest.main()