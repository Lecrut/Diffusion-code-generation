class UniqueCharExtractor:
    def __init__(self):
        self.seen = set()
    
    def extract_unique(self, phrase):
        result = []
        for char in phrase:
            if char not in self.seen:
                self.seen.add(char)
                result.append(char)
        return result

if __name__ == '__main__':
    extractor = UniqueCharExtractor()
    sample_phrase1 = "hello world"
    sample_phrase2 = "Programming is fun"
    sample_phrase3 = "AEIOUaeiou123"
    
    print(extractor.extract_unique(sample_phrase1))
    print(extractor.extract_unique(sample_phrase2))
    print(extractor.extract_unique(sample_phrase3))