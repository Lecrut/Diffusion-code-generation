class ConsonantExtractor:
    def __init__(self):
        self.vowels = 'aeiouAEIOU'

    def extract_and_reverse_consonants(self, phrase):
        consonants = [char for char in phrase if char not in self.vowels]
        return ''.join(consonants[::-1])

if __name__ == '__main__':
    extractor = ConsonantExtractor()
    sample_phrase = 'Hello, World!'
    result = extractor.extract_and_reverse_consonants(sample_phrase)
    print(result)