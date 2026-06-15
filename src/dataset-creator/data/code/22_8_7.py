import unittest
def match_dictionaries(dict1, dict2):
    result = {}
    for key, value in dict1.items():
        if key in dict2 and dict2[key] == value:
            result[key] = value
    return result
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
    def test_partial_match(self):
        dict1 = {'k1': 'v1', 'k2': 'v2'}
        dict2 = {'k1': 'v1', 'k3': 'v3'}
        expected = {'k1': 'v1'}
        self.assertEqual(match_dictionaries(dict1, dict2), expected)
    def test_value_mismatch(self):
        dict1 = {'a': 1}
        dict2 = {'a': 2}
        expected = {}
        self.assertEqual(match_dictionaries(dict1, dict2), expected)
    def test_different_keys(self):
        dict1 = {'a': 1}
        dict2 = {'b': 1}
        expected = {}
        self.assertEqual(match_dictionaries(dict1, dict2), expected)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)