class StringSplitter:
    @staticmethod
    def split_string_by_spaces(s):
        return s.split()

if __name__ == '__main__':
    sample = "Hello World This Is A Test"
    print(StringSplitter.split_string_by_spaces(sample))