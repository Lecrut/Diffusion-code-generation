import unittest

def find_first_element(data):
    if not data:
        return None
    return data[0]

class TestFindFirstElement(unittest.TestCase):
    def test_mixed_types(self):
        mixed_list = ["apple", 3.14, "banana"]
        self.assertEqual(find_first_element(mixed_list), "apple")
        
        float_string_list = [1.0, "hello", 2.5]
        self.assertEqual(find_first_element(float_string_list), 1.0)
        
        only_strings_list = ["a", "b", "c"]
        self.assertEqual(find_first_element(only_strings_list), "a")
        
        only_floats_list = [1.1, 2.2, 3.3]
        self.assertEqual(find_first_element(only_floats_list), 1.1)
        
        empty_list = []
        self.assertIsNone(find_first_element(empty_list))

if __name__ == '__main__':
    sample_mixed_list = ["orange", 2.718, "grape"]
    first_element = find_first_element(sample_mixed_list)
    print(f"The first element is: {first_element}")