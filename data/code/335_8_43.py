class StringSplitter:
    def split(self, s: str, delimiter: str) -> list[str]:
        return [part for part in s.split(delimiter)]
if __name__ == '__main__':
    splitter = StringSplitter()
    test_string = "apple;banana;cherry"
    result = splitter.split(test_string, ";")
    print(result)