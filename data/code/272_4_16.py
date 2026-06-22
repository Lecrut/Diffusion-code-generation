class WordSorter:
    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path

    def read_words(self):
        with open(self.input_file_path, 'r') as file:
            words = file.read().splitlines()
        return words

    def sort_words(self, words):
        return sorted(words)

    def write_words(self, words):
        with open(self.output_file_path, 'w') as file:
            for word in words:
                file.write(word + '\n')

if __name__ == '__main__':
    sorter = WordSorter('sample_input.txt', 'sorted_output.txt')
    words = sorter.read_words()
    sorted_words = sorter.sort_words(words)
    sorter.write_words(sorted_words)