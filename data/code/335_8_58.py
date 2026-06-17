class StringSplitter:
    def split(self, string: str, delimiter: str) -> list[str]:
        if not delimiter:
            raise ValueError("Delimiter cannot be empty")
        return [part for part in string.split(delimiter)]
if __name__ == '__main__':
    splitter = StringSplitter()
    test_string = "apple#banana#cherry"
    result = splitter.split(test_string, "#")
    print(result)