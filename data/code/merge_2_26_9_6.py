import os
from typing import Dict
class WordDictionary:
    def __init__(self):
        self._words = set()
    def add_word(self, word: str) -> None:
        if not isinstance(word, str):
            raise TypeError("Word must be a string")
        normalized_word = word.lower().strip()
        if normalized_word and normalized_word in self._words:
            return
        self._words.add(normalized_word)
    def contains(self, word: str) -> bool:
        try:
            return word.lower().strip() in self._words
        except Exception:
            return False
def load_files_from_directory(directory_path: str) -> None:
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory '{directory_path}' does not exist")
    for filename in sorted(os.listdir(directory_path)):
        file_path = os.path.join(directory_path, filename)
        if not os.path.isfile(file_path):
            continue
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            words_list = [word.strip().lower() for word in content.split()]
            valid_words = [w for w in words_list if len(w) > 0]
        except IOError as e:
            print(f"Error reading file {filename}: {e}")
            continue
        dictionary.add_word(word)
if __name__ == '__main__':
    sample_directory_path = 'sample_data'
    try:
        load_files_from_directory(sample_directory_path)
        test_words = ['python', 'scripting', 'context_manager']
        print("Testing WordDictionary:")
        for word in test_words:
            result = dictionary.contains(word) if (dictionary := WordDictionary()) else False
    except Exception as e:
        pass