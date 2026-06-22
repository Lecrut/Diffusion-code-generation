import csv

class WordSorter:
    INPUT_FILE = 'input.csv'
    OUTPUT_FILE = 'output.csv'

    @staticmethod
    def sort_words_by_first_column(input_file, output_file):
        with open(input_file, mode='r', newline='') as infile:
            reader = csv.reader(infile)
            words = list(reader)
        
        sorted_words = sorted(words, key=lambda row: row[0])
        
        with open(output_file, mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(sorted_words)

if __name__ == '__main__':
    WordSorter.sort_words_by_first_column(WordSorter.INPUT_FILE, WordSorter.OUTPUT_FILE)