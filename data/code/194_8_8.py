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
        data = ["abc", "xyz", "def"]
        self.assertIn(find_longest_string(data), ["abc", "xyz", "def"])
        self.assertEqual(len(find_longest_string(data)), 3)
    def test_longest_at_start(self):
        data = ["longest", "short", "medium"]
        self.assertEqual(find_longest_string(data), "longest")
    def test_longest_at_end(self):
        data = ["short", "medium", "longest"]
        self.assertEqual(find_longest_string(data), "longest")
    def test_with_empty_strings(self):
        data = ["a", "", "bb"]
        self.assertEqual(find_longest_string(data), "bb")
    def test_all_empty_strings(self):
        data = ["", "", ""]
        self.assertEqual(find_longest_string(data), "")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)