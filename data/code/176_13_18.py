class WordExtractor:
    DELIMITERS = '.,!?:; '

    @staticmethod
    def extract_words(text: str) -> list[str]:
        if not text:
            return []
        cleaned_text = ''.join((char.lower() if char.isalnum() else ' ' for char in text))
        words = [word.strip() for word in cleaned_text.split() if word]
        return words
if __name__ == '__main__':
    sample1 = 'Hello world, this is a test.'
    sample2 = ''
    sample3 = '.,!?:; '
    sample4 = 'OneTwoThree'
    sample5 = '   leading and trailing spaces   '
    extractor = WordExtractor()
    print(f"'{sample1}': {extractor.extract_words(sample1)}")
    print(f"'{sample2}': {extractor.extract_words(sample2)}")
    print(f"'{sample3}': {extractor.extract_words(sample3)}")
    print(f"'{sample4}': {extractor.extract_words(sample4)}")
    print(f"'{sample5}': {extractor.extract_words(sample5)}")