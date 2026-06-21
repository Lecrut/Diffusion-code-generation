class WordToKeyMapper:
    def __init__(self):
        self.word_to_key = {}

    def add_mapping(self, word: str, key: int) -> None:
        if not isinstance(word, str) or not isinstance(key, int):
            raise TypeError("Word must be a string and key must be an integer")
        self.word_to_key[word] = key

    def get_key(self, word: str) -> int:
        if word in self.word_to_key:
            return self.word_to_key[word]
        raise KeyError(f"Word '{word}' not found in mapping")

if __name__ == '__main__':
    mapper = WordToKeyMapper()
    mapper.add_mapping("apple", 1)
    mapper.add_mapping("banana", 2)
    mapper.add_mapping("carrot", 3)

    print(mapper.get_key("apple"))
    print(mapper.get_key("banana"))
    print(mapper.get_key("carrot"))