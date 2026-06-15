class SentenceProcessor:
    def split_sentence(self, text: str) -> list[str]:
        return text.split()
if __name__ == '__main__':
    processor = SentenceProcessor()
    long_text = "this is a very long sentence designed to test the efficiency of word splitting on extremely long strings for time and space optimization"
    result = processor.split_sentence(long_text)
    print(result)