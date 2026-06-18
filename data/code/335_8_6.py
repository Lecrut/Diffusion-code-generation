class StringSplitter:
    def split(self, text: str, delimiter: str) -> list[str]:
        return [part for part in self._split_impl(text, delimiter)] if isinstance(delimiter, str) else []
    @staticmethod
    def _split_impl(text: str, delimiter: str) -> list[str]:
        result = []
        start = 0
        while True:
            idx = text.find(delimiter, start)
            if idx == -1:
                break
            result.append(text[start:idx])
            start = idx + len(delimiter)
        else:
            result.append(text[start:])
        return result
if __name__ == '__main__':
    splitter = StringSplitter()
    test_string = "apple;banana;cherry"
    delimiter = ";"
    parts = splitter.split(test_string, delimiter)
    print(parts)