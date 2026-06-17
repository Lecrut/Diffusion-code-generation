class StringSplitter:
    def split(self, string: str, delimiter: str) -> list[str]:
        parts = []
        start = 0
        while True:
            index = string.find(delimiter, start)
            if index == -1:
                break
            end = index + len(delimiter)
            parts.append(string[start:end])
            start = end
        remaining_part = string[start:]
        if remaining_part != '':
            parts.append(remaining_part)
        return parts
if __name__ == '__main__':
    splitter = StringSplitter()
    test_string = "apple,banana,cherry"
    delimiter = ","
    result = splitter.split(test_string, delimiter)
    print(result)