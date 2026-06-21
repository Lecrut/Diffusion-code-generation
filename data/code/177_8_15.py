class TextSplitter:
    @staticmethod
    def split_text(input_string):
        return input_string.split()

if __name__ == '__main__':
    splitter = TextSplitter()
    sample1 = "hello world"
    print(f"Input: '{sample1}'")
    print(f"Output: {splitter.split_text(sample1)}")
    sample2 = "  leading and trailing spaces "
    print(f"Input: '{sample2}'")
    print(f"Output: {splitter.split_text(sample2)}")
    sample3 = "singleword"
    print(f"Input: '{sample3}'")
    print(f"Output: {splitter.split_text(sample3)}")
    sample4 = ""
    print(f"Input: '{sample4}'")
    print(f"Output: {splitter.split_text(sample4)}")