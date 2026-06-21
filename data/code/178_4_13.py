def word_generator(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    yield word.lower()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        raise

class WordIterator:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def get_words(self):
        return word_generator(self.file_path)

if __name__ == '__main__':
    sample_file_path = 'sample.txt'
    word_iter = WordIterator(sample_file_path)
    for word in word_iter.get_words():
        print(word)