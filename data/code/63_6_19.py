import unittest

def find_first_element(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list")
    if not data:
        return None
    return data[0]

class TestFindFirstElement(unittest.TestCase):
    def test_mixed_types(self):
        list_with_strings_and_floats = ["apple", 3.14, "banana"]
        self.assertEqual(find_first_element(list_with_strings_and_floats), "apple")
        
        list_with_floats_and_strings = [1.0, "hello", 2.5]
        self.assertEqual(find_first_element(list_with_floats_and_strings), 1.0)
        
        list_with_only_strings = ["a", "b", "c"]
        self.assertEqual(find_first_element(list_with_only_strings), "a")
        
        list_with_only_floats = [1.1, 2.2, 3.3]
        self.assertEqual(find_first_element(list_with_only_floats), 1.1)
        
        empty_list = []
        self.assertIsNone(find_first_element(empty_list))
    
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            find_first_element("not a list")
        
        with self.assertRaises(ValueError):
            find_first_element(42)

if __name__ == '__main__':
    sample_values = [
        ["apple", 3.14, "banana"],
        [1.0, "hello", 2.5],
        ["a", "b", "c"],
        [1.1, 2.2, 3.3],
        [],
        "not a list",
        42
    ]
    
    for value in sample_values:
        try:
            result = find_first_element(value)
            print(f"First element of {value}: {result}")
        except ValueError as e:
            print(f"Error for input {value}: {e}")