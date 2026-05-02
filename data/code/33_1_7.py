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
    sample2 = "   spaces and    lots of them   "
    sample3 = "nospaceshere"
    print(f"Original: '{sample1}', Processed: '{processor.remove_spaces(sample1)}'")
    print(f"Original: '{sample2}', Processed: '{processor.remove_spaces(sample2)}'")
    print(f"Original: '{sample3}', Processed: '{processor.remove_spaces(sample3)}'")