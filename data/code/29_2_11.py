import unittest

class StringReverser:
    """A class to reverse strings."""

    def __init__(self):
        self.reversed_words = []

    def reverse(self, word) -> str:
        """
        Reverses the input string and adds it to a list of reversed words.

        Args:
            word (str): The string to be reversed.

        Returns:
            str: The reversed version of the input string.
        """
        if isinstance(word, str):
            return word[::-1]
        raise TypeError("Input must be a string.")

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(StringReverserTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

class StringReverserTest(unittest.TestCase):

    def test_reverse_simple(self):
        reverser = StringReverser()
        self.assertEqual(reverser.reverse("hello"), "olleh")

    def test_reverse_empty_string(self):
        reverser = StringReverser()
        self.assertEqual(reverser.reverse(""), "")

    def test_reverse_special_chars(self):
        reverser = StringReverser()
        self.assertEqual(reverser.reverse("!abc!"), "!cba!")

if __name__ == '__main__':
    run_tests()