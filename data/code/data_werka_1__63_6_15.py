import unittest

def find_first_element(data):
    if not data:
        return None
    return data[0]

class TestFindFirstElement(unittest.TestCase):
    def test_mixed_types(self):
        self.assertEqual(find_first_element(["apple", 3.14, "banana"]), "apple")
        self.assertEqual(find_first_element([1.0, "hello", 2.5]), 1.0)
        self.assertEqual(find_first_element(["a", "b", "c"]), "a")
        self.assertEqual(find_first_element([1.1, 2.2, 3.3]), 1.1)
        self.assertIsNone(find_first_element([]))

if __name__ == '__main__':
    sample_list = ["apple", 3.14, "banana"]
    print("First element of sample list:", find_first_element(sample_list))
    
    empty_list = []
    print("First element of empty list:", find_first_element(empty_list))
    
    float_list = [1.0, "hello", 2.5]
    print("First element of float list:", find_first_element(float_list))
    
    string_list = ["a", "b", "c"]
    print("First element of string list:", find_first_element(string_list))