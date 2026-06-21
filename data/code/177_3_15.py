class StringSplitter:
    def split_by_space(self, input_string):
        return input_string.split()

if __name__ == '__main__':
    splitter = StringSplitter()
    test_string = "split this string by spaces"
    result = splitter.split_by_space(test_string)
    print(result)