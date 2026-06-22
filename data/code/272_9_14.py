import csv

class WordSorter:
    INPUT_FILE = 'input.csv'
    OUTPUT_FILE = 'output.csv'

    @staticmethod
    def sort_words_by_first_column():
        with open(WordSorter.INPUT_FILE, mode='r', newline='') as infile:
            reader = csv.reader(infile)
            words = list(reader)

        words.sort(key=lambda row: row[0])

        with open(WordSorter.OUTPUT_FILE, mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(words)

if __name__ == '__main__':
    WordSorter.sort_words_by_first_column()