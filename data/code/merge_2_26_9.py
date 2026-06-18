import os
class WordDictionary:
    def __init__(self):
        self._words = set()
    def add_word(self, word: str) -> None:
        if not isinstance(word, str):
            raise TypeError("Word must be a string")
        self._words.add(word.lower())
    def contains(self, word: str) -> bool:
        return word.lower() in self._words
def load_words_from_files(file_paths: list[str]) -> WordDictionary:
    dictionary = WordDictionary()
    for file_path in file_paths:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            lines = [line.strip() for line in content.split('\n') if line]
            for word_line in lines:
                dictionary.add_word(word_line)
    return dictionary
if __name__ == '__main__':
    sample_files = ['word_list_1.txt', 'word_list_2.txt']
    try:
        my_dict = load_words_from_files(sample_files)
        test_queries = [
            "python",
            "algorithm",
            "nonexistent"
        ]
        for query in test_queries:
            result = my_dict.contains(query)
            print(f"'{query}' found: {result}")
    except FileNotFoundError as e:
        print(f"Error loading files: {e}")