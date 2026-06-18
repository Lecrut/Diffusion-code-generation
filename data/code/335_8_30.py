class StringSplitter:
    def split(self, text: str, delimiter: str) -> list[str]:
        return [part for part in self._split_impl(text, delimiter)]
    @staticmethod
    def _split_impl(text: str, delimiter: str) -> list[str]:
        parts = []
        start = 0
        while True:
            idx = text.find(delimiter, start)
            if idx == -1:
                break
            parts.append(text[start:idx])
            start = idx + len(delimiter)
        parts.append(text[start:])
        return parts
if __name__ == '__main__':
    splitter = StringSplitter()
    sample_text = "apple,banana,cherry"
    delimiter = ","
    result = splitter.split(sample_text, delimiter)
    print(result)