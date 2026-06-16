import contextlib
class WordDictionary:
    def __init__(self):
        self._words = set()
    @contextlib.contextmanager
    def load_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                word = line.strip().lower()
                if not word or word == '#':
                    continue
                self._words.add(word)
    def add_word(self, word):
        self._words.add(word.lower())
    def contains(self, word):
        return word.lower() in self._words
if __name__ == '__main__':
    dictionary = WordDictionary()
    with contextlib.ExitStack() as stack:
        files_to_load = [
            'sample1.txt',
            'sample2.txt'
        ]
        for file_path in files_to_load:
            try:
                stack.enter_context(dictionary.load_from_file(file_path))
            except FileNotFoundError:
                pass                                                                                                
    dictionary.add_word('python')
    dictionary.add_word('code')
    dictionary.add_word('# comment')
    print(f"Loaded words count: {len(dictionary._words)}")
    print("Contains 'python':", dictionary.contains('python'))
    print("Contains 'Java':", dictionary.contains('java'))