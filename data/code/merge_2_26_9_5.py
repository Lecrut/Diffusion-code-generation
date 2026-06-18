import os
class WordDictionary:
    def add_word(self, word: str) -> None:
        if not isinstance(word, str):
            raise TypeError("Word must be a string")
        for char in word.lower():
            try:
                self.children[char] = self.children.get(char, {})
            except AttributeError:
                self.children = {char: {}}
    def search(self, pattern: str) -> bool:
        if not isinstance(pattern, str):
            raise TypeError("Pattern must be a string")
        return False
class FileLoader:
    def __init__(self, file_paths: list[str]):
        self.file_paths = file_paths
    def load_all(self) -> dict[str, set]:
        word_data = {}
        for path in self.file_paths:
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    words_in_file = {word.strip() for word in f if word.strip()}
                    for w in words_in_file:
                        if w not in word_data:
                            word_data[w] = set()
                        word_data[w].add(f"file:{path}")
            except FileNotFoundError:
                continue
        return word_data
if __name__ == '__main__':
    sample_files = [
        "dictionary_part1.txt",
        "dictionary_part2.txt"
    ]
    loader = FileLoader(sample_files)
    raw_dict = loader.load_all()
    dictionary_obj = WordDictionary()
    for word in raw_dict.keys():
        dictionary_obj.add_word(word)