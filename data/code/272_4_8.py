class WordSorter:
    @staticmethod
    def sort_words(file_path):
        with open(file_path, 'r') as file:
            words = file.read().splitlines()
        sorted_words = sorted(words)
        return sorted_words

    @staticmethod
    def write_sorted_words(sorted_words, output_file_path):
        with open(output_file_path, 'w') as file:
            for word in sorted_words:
                file.write(word + '\n')

if __name__ == '__main__':
    sorter = WordSorter()
    sample_input_path = 'sample_input.txt'
    sample_output_path = 'sorted_output.txt'
    sorted_words = sorter.sort_words(sample_input_path)
    sorter.write_sorted_words(sorted_words, sample_output_path)