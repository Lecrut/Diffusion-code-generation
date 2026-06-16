import os
from typing import Dict
class WordDictionary:
    def __init__(self):
        self._words = set()
    def add_word(self, word: str) -> None:
        if not isinstance(word, str):
            raise TypeError("Word must be a string")
        normalized_word = word.strip().lower()
        if normalized_word and normalized_word not in self._words:
            self._words.add(normalized_word)
    def contains(self, word: str) -> bool:
        return word.lower().strip() in self._words
def load_files_to_dictionary(file_paths: list[str]) -> WordDictionary:
    dictionary = WordDictionary()
    for file_path in file_paths:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} does not exist")
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line_num, line in enumerate(lines, start=1):
                word_text = line.strip().split()[0] if len(line.split()) > 0 else ""
                try:
                    dictionary.add_word(word_text)
                except Exception as e:
                    print(f"Error processing file {file_path} at line {line_num}: {e}")
    return dictionary
if __name__ == '__main__':
    sample_files = [
        "input_file_1.txt",
        "input_file_2.txt"
    ]
    try:
        word_dict = load_files_to_dictionary(sample_files)
        test_words = ["apple", "banana", "cherry"]
        for w in test_words:
            result = word_dict.contains(w)
            print(f"Word '{w}' found: {result}")
    except FileNotFoundError as e:
        print(e)