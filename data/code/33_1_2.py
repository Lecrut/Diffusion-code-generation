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
    test_string_2 = "   spaces in this string   "
    test_string_3 = "nospaceshere"
    test_string_4 = ""
    print(f"'{test_string_1}' -> '{processor.remove_spaces(test_string_1)}'")
    print(f"'{test_string_2}' -> '{processor.remove_spaces(test_string_2)}'")
    print(f"'{test_string_3}' -> '{processor.remove_spaces(test_string_3)}'")
    print(f"'{test_string_4}' -> '{processor.remove_spaces(test_string_4)}'")