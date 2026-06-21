def word_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                yield word.lower()

class WordProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def process_words(self):
        return list(word_generator(self.file_path))

if __name__ == '__main__':
    sample_file_path = 'sample.txt'
    processor = WordProcessor(sample_file_path)
    words = processor.process_words()
    print(words)