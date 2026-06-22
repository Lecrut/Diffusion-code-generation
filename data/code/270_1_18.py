class StringProcessor:
    def remove_spaces(self, input_string):
        return ''.join(input_string.split())

if __name__ == '__main__':
    processor = StringProcessor()
    test_string1 = "Hello World! How are you?"
    result1 = processor.remove_spaces(test_string1)
    print(f"Original: '{test_string1}'")
    print(f"Result: '{result1}'")

    test_string2 = "   This has\tmultiple\nspaces.  "
    result2 = processor.remove_spaces(test_string2)
    print(f"Original: '{test_string2}'")
    print(f"Result: '{result2}'")

    test_string3 = "NoSpacesHere"
    result3 = processor.remove_spaces(test_string3)
    print(f"Original: '{test_string3}'")
    print(f"Result: '{result3}'")