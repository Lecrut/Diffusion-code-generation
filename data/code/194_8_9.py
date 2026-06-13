import unittest
def find_longest_string(list_of_strings):
    if not list_of_strings:
        return ""
    longest_string = ""
    max_length = -1
    for s in list_of_strings:
        if len(s) > max_length:
            max_length = len(s)
            longest_string = s
    return longest_string
class TestFindLongestString(unittest.TestCase):
    def test_basic_case(self):
        data = ["apple", "banana", "kiwi"]
        self.assertEqual(find_longest_string(data), "banana")
    def test_empty_list(self):
        data = []
        self.assertEqual(find_longest_string(data), "")
    def test_list_with_one_element(self):
        data = ["hello"]
        self.assertEqual(find_longest_string(data), "hello")
    def test_list_with_identical_lengths(self):
        data = ["abc", "def", "ghi"]
        self.assertEqual(find_longest_string(data), "abc")
    def test_longest_at_start(self):
        data = ["zzzzz", "a", "bb"]
        self.assertEqual(find_longest_string(data), "zzzzz")
    def test_longest_at_end(self):
        data = ["a", "b", "zzzzz"]
        self.assertEqual(find_longest_string(data), "zzzzz")
    def test_all_same_length(self):
        data = ["cat", "dog", "fish"]
        self.assertEqual(find_longest_string(data), "cat")
    def test_empty_strings(self):
        data = ["", "a", ""]
        self.assertEqual(find_longest_string(data), "a")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)