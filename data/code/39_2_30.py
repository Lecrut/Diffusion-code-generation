class SubstringExtractor:
    def __init__(self):
        self.substrings = set()

    def extract(self, text: str, k: int) -> None:
        if k <= 0 or k > len(text):
            return
        n = len(text)
        for i in range(n - k + 1):
            substring = text[i:i+k]
            self.substrings.add(substring)

    def get_unique_substrings(self) -> set:
        return self.substrings

if __name__ == '__main__':
    extractor = SubstringExtractor()
    target_string = "banana"
    substring_length = 2
    extractor.extract(target_string, substring_length)
    result = extractor.get_unique_substrings()
    print(result)