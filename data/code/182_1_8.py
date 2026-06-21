class StringSplitter:
    @staticmethod
    def split_string(input_string):
        return list(input_string)

if __name__ == '__main__':
    splitter = StringSplitter()
    sample_strings = ["hello", "world", "Python"]
    for string in sample_strings:
        result = splitter.split_string(string)
        print(f"Input: {string}, Output: {result}")