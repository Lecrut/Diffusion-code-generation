import unittest

def has_unique_chars(s: str) -> bool:
    if s is None:
        return True
    
    seen = 0
    for char in s:
        code = ord(char)
        if code >= 128:
            continue
        
        if (seen & (1 << code)) > 0:
            return False
        seen |= (1 << code)
    return True

class TestHasUniqueChars(unittest.TestCase):
    def test_basic_unique(self):
        self.assertTrue(has_unique_chars("abcde"))

    def test_basic_dup(self):
        self.assertFalse(has_unique_chars("abcde"))

    def test_single(self):
        self.assertTrue(has_unique_chars("z"))

    def test_empty(self):
        self.assertTrue(has_unique_chars(""))

    def test_all_unique_ascii(self):
        base_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_!"
        self.assertTrue(has_unique_chars(base_str))

    def test_non_ascii_skip(self):
        self.assertTrue(has_unique_chars("ññ"))

if __name__ == '__main__':
    s1 = "python"
    s2 = "hello"
    res1 = has_unique_chars(s1)
    res2 = has_unique_chars(s2)
    print(f"has_unique_chars('{s1}'): {res1}")
    print(f"has_unique_chars('{s2}'): {res2}")
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestHasUniqueChars)
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite)
    print(f"Tests run: {result.testsRun}, Failures: {len(result.failures)}, Errors: {len(result.errors)}")
    print(f"Assertion successful: {result.wasSuccessful()}")