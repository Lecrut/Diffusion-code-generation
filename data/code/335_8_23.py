class StringSplitter:
    def split(self, string: str, delimiter: str) -> list[str]:
        parts = []
        start = 0
        if not string and not delimiter:
            return [string]
        while True:
            index = string.find(delimiter, start)
            if index == -1:
                break
            end_index = index + len(delimiter)
            parts.append(string[start:end_index])
            start = end_index
        parts.append(string[start:])
        return parts
if __name__ == '__main__':
    splitter = StringSplitter()
    test_string = "apple,banana,cherry"
    delimiter = ","
    result = splitter.split(test_string, delimiter)
    print(result)