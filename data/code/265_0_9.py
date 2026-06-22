class PhraseProcessor:
    def __init__(self, phrase):
        self.phrase = phrase

    def extract_even_index_chars(self):
        return ''.join(char for index, char in enumerate(self.phrase) if index % 2 == 0)

if __name__ == '__main__':
    processor = PhraseProcessor("Hello, World!")
    result = processor.extract_even_index_chars()
    print(result)