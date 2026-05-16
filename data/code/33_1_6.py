class StringProcessor:
    def remove_spaces(self, input_string: str) -> str:
        result = []
        for char in input_string:
            if char != ' ':
                result.append(char)
        return "".join(result)
if __name__ == '__main__':
    processor = StringProcessor()
    test_string_1 = "hello world"
    test_string_2 = "   this is a test   "
    test_string_3 = "nospaceshere"
    test_string_4 = " "
    result_1 = processor.remove_spaces(test_string_1)
    result_2 = processor.remove_spaces(test_string_2)
    result_3 = processor.remove_spaces(test_string_3)
    result_4 = processor.remove_spaces(test_string_4)
    print(f"Input: '{test_string_1}', Output: '{result_1}'")
    print(f"Input: '{test_string_2}', Output: '{result_2}'")
    print(f"Input: '{test_string_3}', Output: '{result_3}'")
    print(f"Input: '{test_string_4}', Output: '{result_4}'")