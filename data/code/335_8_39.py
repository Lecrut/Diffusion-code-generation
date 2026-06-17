class StringSplitter:
    def split(self, s: str, delimiter: str) -> list[str]:
        return [part for part in s.split(delimiter)]
if __name__ == '__main__':
    splitter = StringSplitter()
    result = splitter.split("apple,banana,cherry", ",")
    print(result)