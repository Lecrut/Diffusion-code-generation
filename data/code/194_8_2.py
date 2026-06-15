import unittest
def find_longest_string(list_of_strings):
    if not list_of_strings:
        return ""
    longest_string = list_of_strings[0]
    max_length = len(list_of_strings[0])
    for s in list_of_strings[1:]:
        if len(s) > max_length:
            max_length = len(s)
            longest_string = s
    return longest_string
class TestFindLongestString(unittest.TestCase):
    def test_longest_string_basic(self):
        data = ["apple", "banana", "kiwi"]
        self.assertEqual(find_longest_string(data), "banana")
    def test_longest_string_empty_list(self):
        data = []
        self.assertEqual(find_longest_string(data), "")
    def test_longest_string_single_element(self):
        data = ["hello"]
        self.assertEqual(find_longest_string(data), "hello")
    def test_longest_string_identical_lengths(self):
        data = ["abc", "def", "ghi"]
        self.assertEqual(find_longest_string(data), "abc")
    def test_longest_string_with_empty_strings(self):
        data = ["a", "", "bb"]
        self.assertEqual(find_longest_string(data), "bb")
    def test_longest_string_all_empty(self):
        data = ["", "", ""]
        self.assertEqual(find_longest_string(data), "")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)