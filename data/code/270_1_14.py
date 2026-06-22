class StringProcessor:
    def remove_all_spaces(self, input_string):
        return input_string.replace(" ", "")

if __name__ == '__main__':
    processor = StringProcessor()
    
    test_string_1 = "Hello World! How are you?"
    result_1 = processor.remove_all_spaces(test_string_1)
    print(f"Original: '{test_string_1}'")
    print(f"Result: '{result_1}'")
    
    test_string_2 = "   This has\tmultiple\nspaces.  "
    result_2 = processor.remove_all_spaces(test_string_2)
    print(f"Original: '{test_string_2}'")
    print(f"Result: '{result_2}'")
    
    test_string_3 = "NoSpacesHere"
    result_3 = processor.remove_all_spaces(test_string_3)
    print(f"Original: '{test_string_3}'")
    print(f"Result: '{result_3}'")