class StringSplitter:
    def split(self, text: str, delimiter: str) -> list[str]:
        return [part for part in text.split(delimiter)]
if __name__ == '__main__':
    splitter = StringSplitter()
    input_text = "apple;banana;cherry"
    separator = ";"
    result = splitter.split(input_text, separator)
    print(result)