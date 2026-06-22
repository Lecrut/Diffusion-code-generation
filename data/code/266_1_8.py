class WordCounter:
    def __init__(self, filename):
        self.filename = filename

    def count_words(self):
        try:
            with open(self.filename, 'r') as file:
                content = file.read()
                words = content.split()
                return len(words)
        except FileNotFoundError:
            print("File not found.")
            return 0

if __name__ == '__main__':
    counter = WordCounter('sample.txt')
    word_count = counter.count_words()
    print(f"The total number of words is: {word_count}")