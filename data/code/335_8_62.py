import sys
class StringSplitter:
    def split(self, text: str, delimiter: str = ',') -> list[str]:
        return [part for part in text.split(delimiter) if part]
if __name__ == '__main__':
    splitter = StringSplitter()
    sample_text = "apple;banana;cherry"
    result = splitter.split(sample_text, delimiter=';')
    print(result)