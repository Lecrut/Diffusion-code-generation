class WordSorter:
    def __init__(self):
        self.input_path = 'sample_input.txt'
        self.output_path = 'sorted_output.txt'

    def read_words(self):
        with open(self.input_path, 'r') as file:
            words = file.read().splitlines()
        return words

    def sort_words(self, words):
        words.sort()
        return words

    def write_words(self, sorted_words):
        with open(self.output_path, 'w') as file:
            for word in sorted_words:
                file.write(word + '\n')

def main():
    sorter = WordSorter()
    words = sorter.read_words()
    sorted_words = sorter.sort_words(words)
    sorter.write_words(sorted_words)

if __name__ == '__main__':
    main()