class StringSplitter:
    def split_string_by_spaces(self, s):
        return s.split()

if __name__ == '__main__':
    splitter = StringSplitter()
    sample_string = "Hello World This Is A Test"
    result = splitter.split_string_by_spaces(sample_string)
    print(result)