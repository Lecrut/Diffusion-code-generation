class WordGenerator:
    def __init__(self, file_path):
        self.file_path = file_path

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    yield word.lower()

if __name__ == '__main__':
    sample_file_path = 'sample.txt'
    word_gen = WordGenerator(sample_file_path)
    for _ in range(5):
        print(next(word_gen))