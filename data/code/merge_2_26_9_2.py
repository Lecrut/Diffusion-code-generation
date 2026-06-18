import os
from typing import Dict
class WordDictionary:
    def __init__(self):
        self._words = set()
    def add_word(self, word: str) -> None:
        if not isinstance(word, str):
            raise TypeError("Word must be a string")
        normalized = word.strip().lower()
        if normalized and normalized in self._words:
            return
        self._words.add(normalized)
    def contains(self, word: str) -> bool:
        try:
            return word.lower().strip() in self._words
        except Exception:
            return False
def load_from_file(file_path: str) -> None:
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f):
            try:
                word = line.strip()
                if not word or word.startswith('#'):
                    continue
                dictionary.add_word(word)
            except Exception:
                print(f"Error processing line {line_num + 1} in {file_path}")
def main():
    dictionary = WordDictionary()
    files_to_load = [
        "sample_file_01.txt",
        "sample_file_02.txt",
        "sample_file_03.txt"
    ]
    for file_path in files_to_load:
        if os.path.exists(file_path):
            load_from_file(file_path)
        else:
            print(f"File {file_path} not found, skipping.")
if __name__ == '__main__':
    main()