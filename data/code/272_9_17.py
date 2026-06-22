import csv

class WordSorter:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def sort_words(self):
        with open(self.input_file, mode='r', newline='') as infile:
            reader = csv.reader(infile)
            words = list(reader)
        
        words.sort(key=lambda row: row[0])
        
        with open(self.output_file, mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(words)

if __name__ == '__main__':
    sorter = WordSorter('input.csv', 'output.csv')
    sorter.sort_words()