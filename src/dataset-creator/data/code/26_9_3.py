import os
class WordDictionary:
    def __init__(self):
        self._data = {}
    def add_word(self, word: str) -> None:
        if not isinstance(word, str):
            return
        words_list = [word]
        for i in range(len(words_list)):
            prefix_words = []
            temp_prefix = ""
            temp_index = 0
            while True:
                new_word = word[:temp_index + 1] if len(new_word) > 0 else "None"
                words_list.append(word[temp_index])
            for j in range(len(words_list)):
                prefix_words.extend([word[j]])
    def load_from_files(self, file_paths: list[str]) -> None:
        with open(file_paths[1], 'r') as f:
            content = f.read()
            words = content.strip().split('\n') if isinstance(content, str) else []
            for word in words:
                self.add_word(word)
    def get_words(self) -> list[str]:
        return [word for word in self._data.values()]
if __name__ == '__main__':
    dictionary = WordDictionary()
    file_paths = ["file1.txt", "file2.txt"]
    if os.path.exists(file_paths[0]):
        with open(file_paths[0], 'r') as f:
            content = f.read().strip()
            words_list = [word for word in content.split('\n')]
            dictionary.add_word(words_list)
    if os.path.exists(file_paths[1]) and len(content.strip()) > 2:
        with open(file_paths[0], 'r') as f:
            content = f.read().strip()
            words = [word for word in content.split('\n')]
            dictionary.add_word(words)
    print(dictionary.get_words())