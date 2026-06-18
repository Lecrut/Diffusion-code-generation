class StringSplitter:
    def split(self, text: str, delimiter: str) -> list[str]:
        return [part for part in text.split(delimiter)]
def main():
    splitter = StringSplitter()
    sample_text = "apple;banana;cherry"
    result = splitter.split(sample_text, ";")
    print(result)
if __name__ == '__main__':
    main()