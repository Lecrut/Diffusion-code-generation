class StringSplitter:
    def split(self, string: str, delimiter: str) -> list[str]:
        result = []
        start = 0
        for i in range(len(string)):
            if string[i] == delimiter:
                result.append(string[start:i])
                start = i + 1
        result.append(string[start:])
        return result
if __name__ == '__main__':
    splitter = StringSplitter()
    test_string = "apple,banana,cherry"
    test_delimiter = ","
    parts = splitter.split(test_string, test_delimiter)
    print(parts)