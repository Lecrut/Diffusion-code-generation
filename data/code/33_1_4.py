class StringProcessor:
    def remove_spaces(self, input_string: str) -> str:
        result = []
        for char in input_string:
            if char != ' ':
                result.append(char)
        return "".join(result)
if __name__ == '__main__':
    processor = StringProcessor()
    sample1 = "hello world"
    sample2 = "   spaces here   "
    sample3 = "nospaces"
    sample4 = "   "
    print(f"'{sample1}' -> '{processor.remove_spaces(sample1)}'")
    print(f"'{sample2}' -> '{processor.remove_spaces(sample2)}'")
    print(f"'{sample3}' -> '{processor.remove_spaces(sample3)}'")
    print(f"'{sample4}' -> '{processor.remove_spaces(sample4)}'")