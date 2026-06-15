import unittest
def match_dictionaries(dict1, dict2):
    matches = {}
    for key, value1 in dict1.items():
        if key in dict2 and dict2[key] == value1:
            matches[key] = value1
    return matches
class TestMatchDictionaries(unittest.TestCase):
    def test_basic_match(self):
        dict1 = {'a': 1, 'b': 2, 'c': 3}
        dict2 = {'a': 1, 'b': 99, 'd': 4}
        expected = {'a': 1}
        self.assertEqual(match_dictionaries(dict1, dict2), expected)
    def test_all_match(self):
        dict1 = {'x': 10, 'y': 20}
        dict2 = {'x': 10, 'y': 20}
        expected = {'x': 10, 'y': 20}
        self.assertEqual(match_dictionaries(dict1, dict2), expected)
    def test_no_match(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'a': 99, 'b': 100}
        expected = {}
        self.assertEqual(match_dictionaries(dict1, dict2), expected)
    def test_empty_dict1(self):
        dict1 = {}
        dict2 = {'a': 1, 'b': 2}
        expected = {}
        self.assertEqual(match_dictionaries(dict1, dict2), expected)
    def test_empty_dict2(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {}
        expected = {}
        self.assertEqual(match_dictionaries(dict1, dict2), expected)
    def test_both_empty(self):
        dict1 = {}
        dict2 = {}
        expected = {}
        self.assertEqual(match_dictionaries(dict1, dict2), expected)
    def test_value_mismatch(self):
        dict1 = {'k': 10}
        dict2 = {'k': 11}
        expected = {}
        self.assertEqual(match_dictionaries(dict1, dict2), expected)
    def test_key_only_in_dict1(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'a': 1}
        expected = {'a': 1}
        self.assertEqual(match_dictionaries(dict1, dict2), expected)
    def test_key_only_in_dict2(self):
        dict1 = {'a': 1}
        dict2 = {'a': 1, 'b': 2}
        expected = {'a': 1}
        self.assertEqual(match_dictionaries(dict1, dict2), expected)
    def test_complex_values(self):
        dict1 = {'id': 100, 'data': [1, 2]}
        dict2 = {'id': 100, 'data': [1, 2], 'extra': 3}
        expected = {'id': 100, 'data': [1, 2]}
        self.assertEqual(match_dictionaries(dict1, dict2), expected)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)