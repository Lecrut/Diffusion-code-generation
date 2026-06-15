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
        result = match_dictionaries(dict1, dict2)
        self.assertEqual(result, expected)
    def test_no_match(self):
        dict1 = {'a': 1, 'b': 99}
        dict2 = {'a': 1, 'b': 2}
        expected = {'a': (1, 1)}
        result = match_dictionaries(dict1, dict2)
        self.assertEqual(result, expected)
    def test_all_match(self):
        dict1 = {'x': 'hello'}
        dict2 = {'x': 'hello'}
        expected = {'x': ('hello', 'hello')}
        result = match_dictionaries(dict1, dict2)
        self.assertEqual(result, expected)
    def test_no_overlap(self):
        dict1 = {'a': 1}
        dict2 = {'b': 2}
        expected = {}
        result = match_dictionaries(dict1, dict2)
        self.assertEqual(result, expected)
    def test_empty_dict1(self):
        dict1 = {}
        dict2 = {'a': 1, 'b': 2}
        expected = {}
        result = match_dictionaries(dict1, dict2)
        self.assertEqual(result, expected)
    def test_empty_dict2(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {}
        expected = {}
        result = match_dictionaries(dict1, dict2)
        self.assertEqual(result, expected)
    def test_both_empty(self):
        dict1 = {}
        dict2 = {}
        expected = {}
        result = match_dictionaries(dict1, dict2)
        self.assertEqual(result, expected)
    def test_value_mismatch(self):
        dict1 = {'a': 1}
        dict2 = {'a': 2}
        expected = {}
        result = match_dictionaries(dict1, dict2)
        self.assertEqual(result, expected)
    def test_mixed_types(self):
        dict1 = {1: 'one'}
        dict2 = {1: 'one', 2: 'two'}
        expected = {1: ('one', 'one')}
        result = match_dictionaries(dict1, dict2)
        self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)