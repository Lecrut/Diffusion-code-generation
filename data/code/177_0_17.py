class StringSplitter:
    def split_string_by_spaces(self, s):
        return s.split()

if __name__ == '__main__':
    splitter = StringSplitter()
    sample = "Hello World This Is A Test"
    print(splitter.split_string_by_spaces(sample))