import unittest

class ElementFinder:
    @staticmethod
    def find_first_element(data):
        if not data:
            return None
        return data[0]

class TestElementFinder(unittest.TestCase):
    def test_mixed_types(self):
        list_with_strings_and_floats = ["apple", 3.14, "banana"]
        self.assertEqual(ElementFinder.find_first_element(list_with_strings_and_floats), "apple")
        
        list_with_floats_and_strings = [1.0, "hello", 2.5]
        self.assertEqual(ElementFinder.find_first_element(list_with_floats_and_strings), 1.0)
        
        list_with_only_strings = ["a", "b", "c"]
        self.assertEqual(ElementFinder.find_first_element(list_with_only_strings), "a")
        
        list_with_only_floats = [1.1, 2.2, 3.3]
        self.assertEqual(ElementFinder.find_first_element(list_with_only_floats), 1.1)
        
        empty_list = []
        self.assertIsNone(ElementFinder.find_first_element(empty_list))

if __name__ == '__main__':
    sample_data_1 = ["apple", 3.14, "banana"]
    sample_data_2 = [1.0, "hello", 2.5]
    sample_data_3 = ["a", "b", "c"]
    sample_data_4 = [1.1, 2.2, 3.3]
    sample_data_5 = []

    print(ElementFinder.find_first_element(sample_data_1))
    print(ElementFinder.find_first_element(sample_data_2))
    print(ElementFinder.find_first_element(sample_data_3))
    print(ElementFinder.find_first_element(sample_data_4))
    print(ElementFinder.find_first_element(sample_data_5))

    unittest.main(argv=[''], exit=False)