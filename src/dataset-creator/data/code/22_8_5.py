import unittest
def match_dicts(dict1, dict2):
    matches = {}
    for key, val1 in dict1.items():
        if key in dict2 and dict2[key] == val1:
            matches[key] = (val1, dict2[key])
    return matches
class TestMatchDicts(unittest.TestCase):
    def test_basic_match(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'a': 1, 'c': 3}
        expected = {'a': (1, 1)}
        result = match_dicts(dict1, dict2)
        self.assertEqual(result, expected)
    def test_no_match(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'a': 99, 'b': 2}
        expected = {}
        result = match_dicts(dict1, dict2)
        self.assertEqual(result, expected)
    def test_all_match(self):
        dict1 = {'x': 10, 'y': 20}
        dict2 = {'x': 10, 'y': 20}
        expected = {'x': (10, 10), 'y': (20, 20)}
        result = match_dicts(dict1, dict2)
        self.assertEqual(result, expected)
    def test_empty_dict1(self):
        dict1 = {}
        dict2 = {'a': 1, 'b': 2}
        expected = {}
        result = match_dicts(dict1, dict2)
        self.assertEqual(result, expected)
    def test_empty_dict2(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {}
        expected = {}
        result = match_dicts(dict1, dict2)
        self.assertEqual(result, expected)
    def test_both_empty(self):
        dict1 = {}
        dict2 = {}
        expected = {}
        result = match_dicts(dict1, dict2)
        self.assertEqual(result, expected)
    def test_partial_match(self):
        dict1 = {'a': 1, 'b': 2, 'c': 3}
        dict2 = {'a': 1, 'b': 99}
        expected = {'a': (1, 1), 'b': (2, 99)}
        result = match_dicts(dict1, dict2)
        self.assertEqual(result, expected)
    def test_value_mismatch(self):
        dict1 = {'k1': 10}
        dict2 = {'k1': 5}
        expected = {}
        result = match_dicts(dict1, dict2)
        self.assertEqual(result, expected)
    def test_different_keys(self):
        dict1 = {'a': 1}
        dict2 = {'b': 1}
        expected = {}
        result = match_dicts(dict1, dict2)
        self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)