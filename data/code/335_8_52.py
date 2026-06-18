class StringSplitter:
    def split(self, text: str, delimiter: str) -> list[str]:
        if not delimiter:
            raise ValueError("Delimiter cannot be empty")
        return [part for part in text.split(delimiter)]
if __name__ == '__main__':
    splitter = StringSplitter()
    sample_text = "apple;banana,cherry"
    result = splitter.split(sample_text, ";")
    print(result)