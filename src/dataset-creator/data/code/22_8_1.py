import unittest
def match_dictionaries(dict1, dict2):
    matches = {}
    for key, value1 in dict1.items():
        if key in dict2 and dict2[key] == value1:
            matches[key] = (value1, dict2[key])
    return matches
class TestMatchDictionaries(unittest.TestCase):
    def test_basic_match(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'a': 1, 'b': 2, 'c': 3}
        expected = {'a': (1, 1), 'b': (2, 2)}
        self.assertEqual(match_dictionaries(dict1, dict2), expected)
    def test_no_match(self):
        dict1 = {'a': 1, 'b': 99}
        dict2 = {'a': 1, 'b': 2}
        expected = {'a': (1, 1)}
        self.assertEqual(match_dictionaries(dict1, dict2), expected)
    def test_all_match(self):
        dict1 = {'x': 10, 'y': 20}
        dict2 = {'x': 10, 'y': 20}
        expected = {'x': (10, 10), 'y': (20, 20)}
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
        dict1 = {'a': 1}
        dict2 = {'a': 2}
        expected = {}
        self.assertEqual(match_dictionaries(dict1, dict2), expected)
    def test_key_only_in_dict1(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'a': 1}
        expected = {'a': (1, 1)}
        self.assertEqual(match_dictionaries(dict1, dict2), expected)
    def test_key_only_in_dict2(self):
        dict1 = {'a': 1}
        dict2 = {'a': 1, 'b': 2}
        expected = {'a': (1, 1)}
        self.assertEqual(match_dictionaries(dict1, dict2), expected)
    def test_complex_values(self):
        dict1 = {'k1': [1, 2], 'k2': {'x': 10}}
        dict2 = {'k1': [1, 2], 'k2': {'x': 10}, 'k3': 'val'}
        expected = {'k1': ([1, 2], [1, 2]), 'k2': ({'x': 10}, {'x': 10})}
        self.assertEqual(match_dictionaries(dict1, dict2), expected)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)