import unittest

def reverse_string(text: str) -> str:
    """Reverses a given string."""
    return text[::-1]

class TestReverseString(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_normal_case(self):
        expected = "olleh"
        actual = reverse_string("hello")
        self.assertEqual(actual, expected)

    def test_with_spaces(self):
        expected = "ollihs elloh"
        actual = reverse_string("hello world")
        self.assertEqual(actual, expected)

    def test_special_characters(self):
        expected = "!dlroW ,olleh"
        actual = reverse_string("!dlrow ,olleh")
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReverseString)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Run the function with hard-coded sample values for demonstration
    samples = [
        "hello",
        "",
        "a",
        "12345",
        "!@#$%",
        "Python 3.9"
    ]

    print("\n--- Demonstration of reverse_string ---")
    for sample in samples:
        reversed_sample = reverse_string(sample)
        print(f"Original: '{sample}' -> Reversed: '{reversed_sample}'")