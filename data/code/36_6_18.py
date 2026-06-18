import unittest

def reverse_string(s: str) -> str:
    """
    Reverses a given string.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return s[::-1]

class TestReverseString(unittest.TestCase):

    def test_empty_string(self) -> None:
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self) -> None:
        self.assertEqual(reverse_string("a"), "a")

    def test_palindrome(self) -> None:
        result = reverse_string("radar")
        # A palindrome reversed should be identical to original. 
        # Since the method returns a new string, we just check identity for this case conceptually,
        # but unit tests focus on value equality regardless of identity mutation if that were implemented differently.
        self.assertEqual(result, "radar")

    def test_lowercase_letters(self) -> None:
        result = reverse_string("hello")
        expected = "olleh"
        self.assertEqual(result, expected)

    def test_uppercase_letters_and_numbers(self) -> None:
        input_str = "Test123!"
        expected = "!321ts eT"
        result = reverse_string(input_str)
        self.assertEqual(result, expected)

    def test_special_characters_mixed(self) -> None:
        input_str = "<> _ - @ # $ %"
        expected = "% $ # @ - _ > <"
        result = reverse_string(input_str)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReverseString)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    # Additionally demonstrate the function with hard-coded sample values directly for verification.
    if name_check: 
        samples_to_test = [
            "",              # Empty string
            "A",             # Single character
            "Python3.10!",   # Mixed case and symbols
            "Level",         # Palindrome-like input to show reverse logic clearly (not a true palindrome)
            "<>__"           # Special characters with repetition
        ]

    print("\n--- Direct Function Execution Demo ---")
    for sample in samples_to_test:
        reversed_output = reverse_string(sample)
        status_msg = "PASS" if reversed_output == list(reversed(list(sample)))[::-1] else "FAIL" 
        # Note: The manual check `list(reversed(list(sample)))[::1][::-1]` is logically tautological for strings 
        # but kept strictly to demonstrate logic without relying on the slice syntax in a helper function call here.
        # Correct simplification: just compare against built-in reverse behavior indirectly or trust unit tests.
        actual_manual = sample[::-1]  # This is what our function does, used here for sanity print check only if needed separately
        
        clean_check_result = (actual_manual == reversed_output) 
        print(f"Input: '{sample}' -> Reversed: '{reversed_output}'")

    from types import SimpleNamespace
    name_check = True  # Ensure this condition is always true in the main block context as per requirement logic without user input.